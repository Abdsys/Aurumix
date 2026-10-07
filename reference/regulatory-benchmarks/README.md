# Regulatory Benchmarks: Real UAE Token Documents

Public documents filed by real issuers and VASPs under VARA, ADGM FSRA and CBUAE, plus PAXG as the global gold benchmark. Use them to answer "what does good look like" before drafting a whitepaper, a risk disclosure statement or a reserve attestation.

**Retrieved 2026-10-07.** Every PDF was checked as a real PDF (HTTP 200). `.md`, `.txt` and `.html` files are text captures of web pages. Point-in-time copies, not live: re-check the source before you quote one.

## Start here

| Need | File | Regulator |
|---|---|---|
| Whitepaper in the VARA Schedule 1 format (A–F plus the ARVA annex G) | `issuers/Tokinvest_15_GreatHamptonSt_BREI_Whitepaper.pdf` | VARA |
| Schedule 1 whitepaper (Category 2) | `vasps/OKX_ME_BETH_Whitepaper_VARA_Sched1.md`, `vasps/OKX_ME_OKSOL_Whitepaper_VARA_Sched1.md` | VARA |
| Commodity token, 1 token = 1 g | `issuers/Tokinvest_9_SilverBar_Whitepaper.pdf` | VARA |
| Two-token property structure (ownership token plus ARVA management token) | `issuers/ctrlalt/` (2025 TRE versions and Feb 2026 ARVA versions) | VARA |
| Token-specific risk disclosure statement, ranked by materiality | `vasps/OKX_ME_LST_Risk_Disclosure_Statement.md` | VARA |
| Pricing and custody disclosure covering PAXG and ARVA tokens | `vasps/PRYPCO_Mint_BrokerDealer_Disclosure.md` | VARA |
| Per-token circulation and supply disclosure table | `vasps/Roma_VarniLabs_VARA_Disclosures_incl_VA_Offered_Table.md` | VARA |
| Whitepaper the regulator states it accepted | `stablecoins/DDSC_Whitepaper.pdf` | CBUAE |
| Gold reserve attestation (KPMG, monthly, reconciled in ounces) | `stablecoins/Paxos_PAXG_Attestation_KPMG_2026-08-31.pdf` | OCC (US) |
| Gold redemption terms (warehouse-receipt construct) | `stablecoins/Paxos_PAXG_Terms.txt`, `Paxos_PAXG_Whitepaper.pdf` | OCC (US) |
| Reserve attestation citing a UAE rule | `stablecoins/ZandTrust_AEDZ_Attestation_Sep2026.pdf` (PTSR Art. 22) | CBUAE |
| Reasonable-assurance attestation (ISAE 3000) | `stablecoins/UniversalDigital_USDU_Examination_Report_Aug2026.pdf` (COBS 19A.9) | ADGM FSRA |
| Orderly wind-down | `stablecoins/Paxos_USDL_WindDown_Notice.txt` | ADGM FSRA |
| Counter-example: self-certified "audit", up to 10 kg mintable unbacked | `stablecoins/ComtechGold_CGO_*` | DAFZA trade licence only |

## Folders

- **`issuers/`**: documents from VARA Category 1 issuers.
  - Tokinvest: whitepaper, risk disclosure statement and issuer declaration for each offering. Assets: 2 First Gear, 6 LynxCap, 9 Silver Bar, 10 Prudentia, 11 Hottathanafantasy, 15 Great Hampton St, 16 Franklin MMF.
  - Ctrl Alt (`ctrlalt/`): DLD property whitepapers, RDS, policies.
  - PRYPCO Mint terms.
  - MANTRA's MiCA whitepaper, for contrast.
  - `txt/` holds the text extracts.
- **`stablecoins/`**: ADGM and CBUAE fiat-token issuers (USDU, AEDZ, DDSC, AE Coin), Paxos (PAXG, USDG, USDL), Circle USDC, ComTech CGO.
- **`vasps/`**: disclosures from VARA-licensed broker-dealers and exchanges: risk disclosure statements, VA Standards, public disclosures. `supporting/` holds the secondary pages.

## Sources

- Tokinvest documents come from the public documents tab: `portal.tokinvest.capital/asset/{N}/documents`. No login needed. Assets 2, 10, 11 and 16 use signed links that expire after 15 minutes, so the links are dead but these copies are good. Reload the page to get fresh links.
- Ctrl Alt: https://www.ctrl-alt.co/ctrl-alt-solutions-dmcc
- PAXG: https://paxos.com/paxg-transparency
- USDU: https://universal.ae/transparency
- AEDZ: https://zandtrust.com/en
- DDSC: https://ddsc.ai
- AE Coin: https://aecoin.com
- OKX ME: `okx.com/en-ae/help/okx-middle-east-*`
- PRYPCO: https://prypco.com/mint/broker-dealer-disclosure
- Roma: https://roma.global/disclosures

## Caveats

- **No VARA issuer publishes a reserve attestation report.** Reserves appear only as text inside the whitepapers.
- **No document discloses stress testing.**
- **Zand AEDZ attestation:** signed by AJMS LG Management Consulting, although the Zand FAQ names Crowe.
- **DDSC dashboard:** stale (1 May 2026).
- **AEDZ whitepaper:** scanned images with no text layer. Run OCR before searching it.
- **Coverage:** VARA issuers beyond Tokinvest and Ctrl Alt were not swept (search budget ran out). Neither were around 20 smaller VASPs on the NeosLegal map.
