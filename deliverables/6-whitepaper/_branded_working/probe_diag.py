# Probe natural diagram sizes under candidate layout-only settings.
#   python probe_diag.py "<flowchart json>" "<sequence json>"  -> writes probe.html
import sys, io, os, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_wp as B
fc = sys.argv[1] if len(sys.argv) > 1 else "{}"
sq = sys.argv[2] if len(sys.argv) > 2 else "{}"
d = B.load_maps()
body = ""
for wp, v in d.items():
    code = v["code"]
    body += '<div class="d" data-wp="%s"><div class="mermaid">%s</div></div>\n' % (wp, html.escape(code, quote=False))
page = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>body{font-family:'Libre Franklin'} .d{width:2000px}</style></head><body>%s
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
var fc=%s, sq=%s;
mermaid.initialize({startOnLoad:false,securityLevel:'loose',theme:'base',themeVariables:{fontSize:'14px'},
 flowchart:Object.assign({nodeSpacing:30,rankSpacing:35,useMaxWidth:false},fc),
 sequence:Object.assign({mirrorActors:false,actorMargin:40,width:130,height:50,messageMargin:32,boxMargin:8,noteMargin:8,useMaxWidth:false},sq)});
(async function(){await document.fonts.ready; await mermaid.run({querySelector:'.mermaid'});
 var out=[];document.querySelectorAll('.d').forEach(function(e){var s=e.querySelector('svg');var vb=s.viewBox.baseVal;out.push(e.dataset.wp+' '+Math.round(vb.width)+'x'+Math.round(vb.height));});
 document.body.setAttribute('data-out',out.join(' | '));})();
</script></body></html>""" % (body, fc, sq)
io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "probe.html"), "w", encoding="utf-8").write(page)
