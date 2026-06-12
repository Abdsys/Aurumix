const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  LevelFormat, PageBreak
} = require('docx');
const fs = require('fs');
const path = require('path');

const NPM_MODULES = 'C:/Users/BlockApex/AppData/Roaming/npm/node_modules';
require('module').globalPaths.push(NPM_MODULES);

const heading = (text, level) => new Paragraph({
  heading: level,
  children: [new TextRun({ text })],
});

const para = (text, opts = {}) => new Paragraph({
  spacing: { after: 120 },
  children: [new TextRun({ text, ...opts })],
});

const bullet = (text) => new Paragraph({
  numbering: { reference: 'bullets', level: 0 },
  spacing: { after: 60 },
  children: [new TextRun({ text })],
});

const numbered = (text, ref) => new Paragraph({
  numbering: { reference: ref, level: 0 },
  spacing: { after: 60 },
  children: [new TextRun({ text })],
});

const numberedHeading = (text, ref) => new Paragraph({
  numbering: { reference: ref, level: 0 },
  spacing: { before: 180, after: 60 },
  children: [new TextRun({ text, bold: true })],
});

const numberingConfig = [
  { reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
  { reference: 'chrono', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
  { reference: 'sustain', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
];

const styles = {
  default: { document: { run: { font: 'Arial', size: 22 } } },
  paragraphStyles: [
    { id: 'Title', name: 'Title', basedOn: 'Normal',
      run: { size: 48, bold: true, color: '000000', font: 'Arial' },
      paragraph: { spacing: { before: 0, after: 240 }, alignment: AlignmentType.LEFT } },
    { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
      run: { size: 32, bold: true, color: '000000', font: 'Arial' },
      paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
    { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
      run: { size: 26, bold: true, color: '000000', font: 'Arial' },
      paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
    { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
      run: { size: 22, bold: true, color: '333333', font: 'Arial' },
      paragraph: { spacing: { before: 180, after: 100 }, outlineLevel: 2 } },
  ],
};

const children = [];

children.push(new Paragraph({
  heading: HeadingLevel.TITLE,
  children: [new TextRun({ text: 'Aurumix Project Summary' })],
}));

children.push(heading('What It Is, In Plain Terms', HeadingLevel.HEADING_1));
children.push(para('Aurumix is a gold-backed long-term savings programme dressed up as a crypto token. Investors commit to monthly contributions (a SIP). Every dollar is split 70% into physical gold (held in a Dubai LBMA vault) and 30% into a conservative bond portfolio. Investors receive AURX tokens representing their share of the pool. New tokens are released every 15 days through "Mining Events" at a price the company itself calculates by formula. Headquartered in Dubai under VARA regulation, targeting NRI, HNI, and diaspora retail investors over a 50-year horizon.'));
children.push(para('The mental model the founders push: Aurumix is the company. AURX is the share. Gold and bonds are the assets. Mining Events are rights issues.'));

children.push(heading('Chronology', HeadingLevel.HEADING_1));

const chronoSections = [
  { title: 'Project Launches', items: [
    'All 100 billion AURX tokens minted at once into the Genesis Contract (hard cap, no more ever)',
    'Smart contracts deployed for split, mining, locks, fees, custody',
    'Founders buy at the same price as everyone else (no free tokens)',
  ] },
  { title: 'First Mining Event', items: [
    '$10,000 total event size, AURX priced at $0.00125',
    '8 million tokens released',
    'Earliest investors fill the event',
  ] },
  { title: 'Investor Joins', items: [
    'Downloads the Aurumix Circle app, completes KYC',
    'Sets up monthly SIP: amount, duration (6 months to 25 years), lock-in period, family group, referrer',
    'Auto-debit mandate registered',
  ] },
  { title: 'Each Monthly Payment', items: [
    'Smart contract splits the money instantly: 70% buys gold, 30% goes to the bond pool',
    "Investor's ICS (Investor Conviction Score) updates: streak +1, duration logged",
    'After 6 consecutive events, the investor earns Confirmed SIP status. Their fixed monthly amount is now guaranteed allocation in every future event',
  ] },
  { title: 'Mining Events Every 15 Days', items: [
    'Custodian confirms the gold is in the vault',
    'Price calculated: GFV (gold value per token) + APV (algo pool premium)',
    'Price can only go up, never down',
    '95% of new tokens go to SIP investors (allocated by Priority Score)',
    '5% reserved as a Spot Window for high-tier members (activates after Year 2)',
    'Fees deducted, tokens distributed, dashboards refresh',
  ] },
  { title: 'Status Climbing Over Time', items: [
    'Priority Score builds from SIP × Duration × Lock × Continuity × Family × Referrals',
    'Investors climb six tiers (Silver to Sovereign), each unlocking spot access and better allocation',
  ] },
  { title: 'Year 2 Exchange Listing', items: [
    'AURX lists on CEX and DEX',
    'Two parallel prices emerge: Mining Event Price (formula-driven, never falls) and Secondary Market Price (free float)',
    'Spot Window fully activates',
  ] },
  { title: 'Liquidity Without Selling', items: [
    'Investor pledges AURX to a smart contract',
    'Borrows against the gold value (74% for Gold tier, higher for higher tiers)',
    'Delivered through local partners (NBFC in India, prepaid wallet, debit card)',
    'Investor spends through credit instead of selling tokens',
  ] },
  { title: 'The Long Arc', items: [
    'Years 1 to 15: ~70% of supply released, high oversubscription, demand engine active',
    'Years 16 to 50: ~30% of supply released, premium compresses, ecosystem matures',
    'Algo Growth Fee declines from 5% to 2% floor by ~Year 13',
    'Target: 100,000+ investors per event by Year 50',
  ] },
  { title: 'Exit (Or Not)', items: [
    'Lock-in expires. Tokens can be transferred or sold',
    'The design discourages selling. The credit facility lets investors spend their gold value without selling',
    'Built so investors never exit, only spend',
  ] },
];

chronoSections.forEach(s => {
  children.push(numberedHeading(s.title, 'chrono'));
  s.items.forEach(i => children.push(bullet(i)));
});

children.push(heading('Sustainability Issues', HeadingLevel.HEADING_1));
children.push(para('These are not edge cases. They are baked into the design.'));

const sustain = [
  { title: 'The Company Sets Its Own Price', text: 'Aurumix calculates the Mining Event price using a formula it controls. One input, the V3 "target alignment multiplier", is designed to adjust prices upward when investor growth falls short of plan. That is not pricing. That is calibration to a business target. No independent body, no market, and no audit verifies the price at issuance. The team that earns fees on the algo pool is the same team that sets the algo pool\'s quoted value.' },
  { title: 'Price Drifts Above Real Asset Value Over Time', text: 'The price formula is Gold Floor Value + Algo Pool Premium. The Algo Pool Premium grows by V1 + V2 + V3 every event. V2 alone adds 6% annually with no underlying cashflow justifying it. V3 adds far more in early years. Real bond yields earned on the algo pool are 4 to 5%. The result: the official Mining Event price grows faster than the asset base behind each token. The longer the project runs, the wider the gap between what investors pay at events and what each token represents in real assets.' },
  { title: 'Price Floor Goes Only One Way', text: 'Mining Event price can never decrease. Even if gold drops 30%, even if the bond portfolio loses value, the next event price must be at or above the previous one. This is enforced by smart contract. It creates a mathematical commitment that may eventually be impossible to honour without inflating V3, which deepens the previous problem.' },
  { title: 'There Is No Redemption At Event Price', text: 'A real SIP lets you redeem at NAV. Aurumix removes that right entirely, framed as "IPO model, not redemption fund". The investor can only sell on the secondary market, where price will be whatever buyers will pay. The Mining Event price has no market test. If many investors try to exit at once, the secondary market collapses while the Mining Event price keeps quoting higher numbers to new investors.' },
  { title: 'The System Depends on Continuous Oversubscription', text: 'The event sizing formula, the V3 multiplier, and the price floor all depend on consistent oversubscription event after event. If new investor inflows slow, demand pressure fails. V3 has to work harder to hit the trajectory. The gap between price and NAV widens. Confidence breaks. The model has no graceful failure mode for low growth. It can only contract supply, not adjust price downward.' },
  { title: 'Late Investors Get Worse Deals By Design', text: 'An investor who joins in Year 20 buys at a price reflecting 20 years of compounded V2 and V3 markups. The gold per token they receive is smaller than what an early investor received per dollar invested. Existing holders benefit from each new investor entering at a higher price. Early investors are paid by late investors entering at premium. That is the textbook critique of any compounding-price model.' },
  { title: 'Long Lock-ins Hide The Problem', text: 'Lock-ins of 6 months to 25 years, combined with credit facilities that let investors spend without selling, mean the model can run for years without anyone testing the real price. The Mining Event price keeps going up. Investors think they are winning. The reality check only arrives if regulators intervene, exchange listings expose the gap, or an external shock forces simultaneous exit.' },
];

sustain.forEach(s => {
  children.push(numberedHeading(s.title, 'sustain'));
  children.push(para(s.text));
});

children.push(heading('Design Gaps', HeadingLevel.HEADING_1));
children.push(para('If we take the design as-is, these are the open items that need to be closed before anything downstream is meaningful.'));

children.push(heading('Formulas Marked "Need To Work" In Their Own Doc', HeadingLevel.HEADING_2));
[
  'V3 formula itself. Trajectory described (100% to 8% to 5%), formula not built. Target Alignment Multiplier not specified.',
  'Duration Score values across all 10 SIP bands',
  'Lock-in Score values across all 10 lock bands',
  'Subscription Adjustment %s in the high-demand bands (SR > 2.0×)',
  'Custody fee % (currently ~1%, depends on actual cost)',
  'Loyalty Multiplier appears in the Priority Score formula but is never defined',
  'Class Multiplier values for the I to V investor classes',
  'Decay constants across the 50-year supply curve',
].forEach(b => children.push(bullet(b)));

children.push(heading('Mechanics Described But Underspecified', HeadingLevel.HEADING_2));
[
  'ICS Score formula itself. Tier ranges are given but the calculation from inputs is missing.',
  'Confirmed SIP threshold logic. 6 events confirmed, but the allocation algorithm around the protected base is fuzzy.',
  'Phase 1 vs Phase 2 supply split. Stated as ~70% and ~30%, exact decay schedule not defined.',
  'Spot Window allocation post-Y2. Activation trigger, residual roll-up edge cases, streak bonus interaction.',
  'Family Group SIP splitting rules. How a $100 SIP is split across 8 family members, who counts towards the bonus.',
  'Investor Class System thresholds. $37.50/event appears arbitrary, not derived.',
  'Mining Event Scheduler governance. Multi-sig approval rules, what changes require it, frozen periods.',
  'Credit limit % per tier. Only Gold tier example (74%) given. Other tiers not specified.',
  'Streak recovery math. "Held points reactivate" but the formula for partial reactivation is missing.',
].forEach(b => children.push(bullet(b)));

children.push(heading('Missing Entirely', HeadingLevel.HEADING_2));
[
  "Tony's two-sided spend matching. Buyer's cash pays seller's credit balance, seller's tokens transfer to buyer. Zero pool impact. Came up in the meeting, not in the doc.",
  'Secondary market liquidity strategy. DEX vs CEX, depth requirements, market making arrangements, anti-slippage rules.',
  'Cohort-level fee revenue model. The doc explicitly asks for this in Section 2.6 but does not have it.',
  'Aggregate fee revenue curve from 500 investors in Year 1 to 100K in Year 10. Not modeled.',
  'Bank interest accrual rules for the algo pool. How it nets against fees, replenishes the floor.',
  'Gold price oracle fallback logic. What happens if Chainlink fails, if LBMA fix is delayed.',
  'Founder allocation cohort modeling. Full parity is claimed but no cohort-level proof.',
  'Cross-border delivery specifics beyond the 5-route table. NBFC partner selection, capital flows, settlement.',
  'Stress test scenario parameters. Pool depletion, gold crash, oversubscription failure, redemption shock.',
  'NAV vs Event Price gap reporting. No published methodology.',
  'Early exit penalty schedule. Lock-in mechanism exists, penalty curve undefined.',
  'Agent commission tunable bounds. "Can be adjusted via governance" but no rules on bounds.',
].forEach(b => children.push(bullet(b)));

children.push(heading('Ambiguous Or Unresolved', HeadingLevel.HEADING_2));
[
  'Token standard. ERC-20 implied but ERC-3643 or ERC-1400 needed for VARA compliance. Not chosen.',
  'Spot Window timing. Activates "post-Y2" but specific event trigger not defined.',
  'VARA classification ruling. They hope for "commodity-linked hybrid". Not confirmed.',
  'MLM safe harbor design. Referral cap stated as "subordinate to investment scores" but the actual cap % not set.',
  'Custody multi-vault failover. Brinks, Loomis, Malca-Amit listed as options. Single or split?',
  'Algo pool instrument allocation %s. Govt securities, MMF, IG bonds, deposits all listed. Target allocation not specified.',
  'Subscription Ratio definition. Capital blocked vs planned capital, but planned capital itself adjusts. Circular.',
].forEach(b => children.push(bullet(b)));

children.push(para('The Mechanism Design phase has to close the first two categories before any simulation work is meaningful. The third category is design additions worth pitching as scope. The fourth needs legal and architectural decisions, not just math.'));

children.push(heading('Summary', HeadingLevel.HEADING_1));
children.push(para('The structure works if and only if new investors keep showing up faster than old investors want to exit. The 70% gold backing is real and provides a meaningful floor. The 30% algo pool\'s quoted growth is largely algorithmic markup. The legal structure (no redemption right) protects Aurumix from a bank run. It does not protect the investor from buying into a price detached from underlying value.'));
children.push(para('These are solvable problems. Solving them requires changes to the pricing formula, the floor rule, and the disclosure framework. Better simulations of the current design will not fix it.'));

const doc = new Document({
  styles,
  numbering: { config: numberingConfig },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children,
  }],
});

const outPath = path.join(__dirname, 'Aurumix_Summary.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outPath, buf);
  console.log('Wrote ' + outPath + ' (' + (buf.length / 1024).toFixed(1) + ' KB)');
});
