  (function(){
    'use strict';
    var BUFFER=2;
    function isAtomic(el){
      if(!el||el.nodeType!==1)return false;
      var s=window.getComputedStyle(el);
      var bi=s.getPropertyValue('break-inside')||s.getPropertyValue('-webkit-break-inside');
      if(bi==='avoid')return true;
      var t=el.tagName.toLowerCase();
      if(t==='table'||t==='figure'||t==='blockquote')return true;
      if(el.classList.contains('callout')||el.classList.contains('pull-quote')||
         el.classList.contains('stat-row')||el.classList.contains('finding')||
         el.classList.contains('keep-together'))return true;
      return false;
    }
    function isWrapper(el){
      if(!el||el.nodeType!==1)return false;
      if(el.tagName.toLowerCase()!=='div')return false;
      if(el.hasAttribute('data-text-role')&&el.children.length>1)return true;
      return false;
    }
    function flattenWrappers(ca){
      var changed=true;
      while(changed){changed=false;
        var ch=Array.prototype.slice.call(ca.children);
        for(var i=0;i<ch.length;i++){
          if(isWrapper(ch[i])){
            var w=ch[i],p=w.parentNode,nx=w.nextSibling;
            var inner=Array.prototype.slice.call(w.children);
            for(var j=0;j<inner.length;j++)p.insertBefore(inner[j],nx);
            p.removeChild(w);changed=true;break;
          }
        }
      }
    }
    function makeCont(orig){
      var c=document.createElement('div');
      c.className=orig.className;
      c.setAttribute('data-template',orig.getAttribute('data-template')||'');
      c.setAttribute('data-auto-continue','');
      c.setAttribute('data-continuation','');
      var ca=document.createElement('div');
      ca.className='content-area';
      c.appendChild(ca);
      var pn=document.createElement('div');
      pn.className='page-number';
      pn.setAttribute('data-text-role','page-number');
      c.appendChild(pn);
      return c;
    }
    function getCA(p){return p.querySelector('.content-area');}
    function neutralizeLayout(ca){
      var cs=window.getComputedStyle(ca);
      if(cs.display==='flex'||cs.display==='inline-flex'||cs.overflow==='hidden'){
        ca.style.display='block';ca.style.flexDirection='';ca.style.overflow='visible';
      }
    }
    function process(page){
      var ca=getCA(page);
      if(!ca)return[page];
      flattenWrappers(ca);
      neutralizeLayout(ca);
      var uh=ca.clientHeight-BUFFER;
      if(ca.scrollHeight<=uh+BUFFER){page.setAttribute('data-auto-continued','');return[page];}
      var ch=[];for(var i=0;i<ca.children.length;i++)ch.push(ca.children[i]);
      var si=-1,ar=ca.getBoundingClientRect();
      for(var i=0;i<ch.length;i++){
        if(ch[i].classList.contains('page-number'))continue;
        if(ch[i].getBoundingClientRect().bottom-ar.top>uh){si=i;break;}
      }
      if(si===-1){page.setAttribute('data-auto-continued','');return[page];}
      var oc=ch[si];
      if(oc.getBoundingClientRect().top-ar.top<uh&&isAtomic(oc)){/* straddles — move whole */}
      var nd=0;
      for(var n=0;n<ch.length;n++){
        if(!ch[n].classList.contains('page-number')&&
           !ch[n].classList.contains('content-heading')&&
           ch[n].tagName.toLowerCase()!=='hr')nd++;
      }
      if(si===0&&nd<=1){page.setAttribute('data-auto-continued','');return[page];}
      while(si>1){var pv=ch[si-1];if(!pv||pv.nodeType!==1)break;var pt=pv.tagName.toLowerCase();if(pt==='h3'||pt==='h4'||pt==='h5'){si--;}else{break;}}
      var cp=makeCont(page);
      page.parentNode.insertBefore(cp,page.nextSibling);
      var cca=getCA(cp),tm=[];
      for(var j=si;j<ch.length;j++){if(!ch[j].classList.contains('page-number'))tm.push(ch[j]);}
      for(var k=0;k<tm.length;k++)cca.appendChild(tm[k]);
      page.setAttribute('data-auto-continued','');
      return[page].concat(process(cp));
    }
    function renumber(){
      var pp=document.querySelectorAll('#document-pages > .page');
      var pageNum=1;
      for(var i=0;i<pp.length;i++){
        var pg=pp[i];
        // Skip cover, TOC, and closing cover pages - they don't get numbered
        if(pg.classList.contains('page--cover-minimal-typographic'))continue;
        if(pg.classList.contains('page--special-table-of-contents'))continue;
        if(pg.classList.contains('page--closing-back-cover'))continue;
        var n=pg.querySelector('.page-number');
        if(n)n.textContent=String(pageNum++);
      }
    }
    function populateTOC(){
      var ee=document.querySelectorAll('.toc-entry[data-toc-ref]');
      if(ee.length===0)return;
      for(var i=0;i<ee.length;i++){
        var ref=ee[i].getAttribute('data-toc-ref');if(!ref)continue;
        var t=document.getElementById(ref);
        if(!t)t=document.querySelector('.page[data-toc-id="'+ref+'"]');
        if(!t)continue;
        var pg=t.closest?t.closest('#document-pages > .page'):null;
        if(!pg){var nd=t;while(nd&&nd!==document.body){if(nd.classList&&nd.classList.contains('page')&&nd.parentNode&&nd.parentNode.id==='document-pages'){pg=nd;break;}nd=nd.parentNode;}}
        if(!pg&&t.classList&&t.classList.contains('page'))pg=t;
        if(!pg)continue;
        var nm=pg.querySelector('.page-number');if(!nm)continue;
        var sp=ee[i].querySelector('.toc-entry-page');if(sp)sp.textContent=nm.textContent;
      }
    }
    function fixLastPageBreak(){
      var lastPage=document.querySelector('#document-pages > .page:last-child');
      if(lastPage){
        lastPage.style.pageBreakAfter='auto';
        lastPage.style.breakAfter='auto';
      }
    }
    function run(){
      var pp=document.querySelectorAll('.page[data-auto-continue]');
      if(pp.length===0){renumber();populateTOC();fixLastPageBreak();document.dispatchEvent(new Event('auto-continue-complete'));return;}
      var a=Array.prototype.slice.call(pp);
      for(var i=0;i<a.length;i++)process(a[i]);
      renumber();populateTOC();fixLastPageBreak();
      document.dispatchEvent(new Event('auto-continue-complete'));
    }
    function waitForMermaid(){
      return new Promise(function(resolve){
        if(typeof mermaid==='undefined'){resolve();return;}
        var dd=document.querySelectorAll('.mermaid');
        if(dd.length===0){resolve();return;}
        var att=0,max=100;
        function chk(){
          var ok=true;
          for(var i=0;i<dd.length;i++){if(!dd[i].querySelector('svg')){ok=false;break;}}
          if(ok||att>=max){resolve();}else{att++;setTimeout(chk,100);}
        }
        chk();
      });
    }
    if(document.readyState==='loading'){
      document.addEventListener('DOMContentLoaded',function(){document.fonts.ready.then(function(){return waitForMermaid();}).then(run);});
    }else{document.fonts.ready.then(function(){return waitForMermaid();}).then(run);}
  })();
