"""
Aurumix Revenue Model - Excel Workbook Builder
===============================================

Built from : deliverables/4-revenue-modeling/Aurumix_Revenue_Model_Architecture_Brief.md
Standard   : DRODE_Revenue_Model_V3.xlsx (the firm's reference build)

FIVE SHEETS: Cover | Assumptions | Scenario Parameters | Model | Summary

    Assumptions  A=Parameter  B=Value(BLUE)  C=Unit  D=Source
    Scenario     A=Parameter  B=Active  C=Base  D=Aggressive  E=Conservative
    Model        R2=Period #  R3=Period,  periods in C..AE (29)
    Summary      year columns D..J (Y1..Y7)

Colours: BLUE = input, BLACK = in-sheet formula, GREEN = cross-sheet reference.

Periods: 29 = 24 monthly (M1-M24) + 5 annual (Y3-Y7). M1 = January 2027.

-----------------------------------------------------------------------------
SIMPLIFICATION AGREED 2026-08-20. This is a REVENUE model.
-----------------------------------------------------------------------------
DELETED (moved to the Phase 5 simulation, where heterogeneity belongs):
  - five payment archetypes and their weights / pay probabilities / hazards
  - the run-of-6 first-passage gate chain
  - the 84-month lifecycle curves and the convolution
  - the six-state machine, the REDUCED state, the withdrawal-bucket distribution

REPLACED BY a rolling balance the client can read:
    opening + new - churned = closing

KEPT DELIBERATELY, because dropping each changes the answer by more than the
simplification saves:
  1. ELIGIBILITY as two input cells - "% who ever qualify" and "months to
     qualify". The card streams are ~83% of gross profit and all hang off the
     six-payment gate; assuming everyone qualifies overstates by ~59%. The
     archetype engine's OUTPUT (55%, M8) becomes these two inputs.
  2. A HOLDERS balance. Customers who stop paying KEEP THEIR GOLD - they stay
     in AUM, custody, collateral and the B2B base, and reach ~81% of everyone
     ever acquired by Y6. Without it AUM and streams 5/6 are badly understated.
  3. The FABRICATION PREMIUM inside stream 1. The entry fee is a MARGIN, not a
     fee: 5% charged less ~1.5% to buy the metal. Gross would read ~43% high.
     This is cost OF REVENUE, not opex.
  4. The ATM draw distribution (4 rows). The mean draw sits just below the free
     allowance BY DESIGN, so a mean returns EXACTLY ZERO over-allowance revenue.

OUT OF SCOPE for now, to be bolted on later: opex, headcount, tax, working
capital, cash, funding, break-even. The model reports revenue and gross margin.
"""

import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "Aurumix_Revenue_Model.xlsx")

# ============================================================================
# BRAND
# ============================================================================
WARM_CHARCOAL, GOLD, DARK_GOLD, STONE, STONE_LIGHT = "1A1714", "B8956E", "96734A", "D4CFC8", "E8E4DF"
BLUE, BLUE_BOLD = Font(color="0000FF"), Font(color="0000FF", bold=True)
BLACK, BLACK_BOLD = Font(color="000000"), Font(color="000000", bold=True)
GREEN, GREEN_BOLD = Font(color="009B73"), Font(color="009B73", bold=True)
RED_BOLD = Font(color="C00000", bold=True)

SECTION_FILL = PatternFill("solid", fgColor=WARM_CHARCOAL)
HEADER_FILL = PatternFill("solid", fgColor=STONE)
BANNER_FILL = PatternFill("solid", fgColor=STONE_LIGHT)

COVER_TITLE = Font(size=24, bold=True, color=GOLD)
COVER_SUB = Font(size=16, color=WARM_CHARCOAL)
SHEET_TITLE = Font(size=18, bold=True, color=GOLD)
SHEET_SUB = Font(size=14, bold=True, color=WARM_CHARCOAL)
SECTION_FONT = Font(size=11, bold=True, color="FFFFFF")
BANNER_FONT = Font(size=11, bold=True, color=WARM_CHARCOAL)
HEADER_FONT = Font(size=10, bold=True, color=WARM_CHARCOAL)
SECONDARY = Font(size=9, color=DARK_GOLD)
NOTE_FONT = Font(size=9, italic=True, color=DARK_GOLD)

STONE_THIN = Side(style="thin", color=STONE)
BORDER = Border(top=STONE_THIN, bottom=STONE_THIN, left=STONE_THIN, right=STONE_THIN)
TOTALS_BORDER = Border(top=Side(style="thin", color=GOLD), bottom=Side(style="double", color=GOLD))

FMT_USD, FMT_USD2 = '$#,##0;($#,##0);"-"', '$#,##0.00;($#,##0.00);"-"'
FMT_NUM, FMT_NUM2, FMT_NUM3 = '#,##0;(#,##0);"-"', '#,##0.00;(#,##0.00);"-"', '#,##0.000'
FMT_PCT, FMT_PCT2 = '0.0%', '0.00%'
UNFILLED = "{{UNFILLED}}"

# ============================================================================
# PERIOD GRID
# ============================================================================
N_MONTHLY, N_ANNUAL = 24, 5
N_PERIODS = N_MONTHLY + N_ANNUAL
PCOL0, START_YEAR = 3, 2027
SUMCOL0, N_YEARS = 4, 7
REGIONS = ["uae", "gulf", "india"]
RLAB = {"uae": "UAE", "gulf": "Oman and Bahrain", "india": "India"}
RDESC = {
    "uae": "UAE residents - Indian plus other South Asian (Pakistani, Bangladeshi, Sri Lankan, Nepali). "
           "COMBINED 2026-08-20 from two separate regions: both sit under one licence, one set of rails and "
           "one agent channel, both open at M1, and both are UAE-resident for VAT. They differed only on "
           "average ticket (USD 38 vs USD 26), which the blended USD 33.60 preserves at the book level. The "
           "core market - the gold-savings habit and the agent network originate here.",
    "gulf": "Expatriate workers in Oman and Bahrain. ~600,000 addressable. NOT UAE-resident, so VAT and "
            "reporting treatment differ. Requires local authorisation in a second and third jurisdiction, "
            "which is why it is the only staged region.",
    "india": "India-resident retail investors. ~12.5m addressable, sized BEHAVIOURALLY from gold ETF folios "
             "intersected with active digital-gold holders rather than demographically. The payment route is "
             "ASSUMED SOLVED in this model - if it is not, this region does not open at all.",
}


def pcol(i):  return get_column_letter(PCOL0 + i)
def pcell(r, i): return "%s%d" % (pcol(i), r)
def ycol(y):  return get_column_letter(SUMCOL0 + y - 1)
def is_monthly(i): return i < N_MONTHLY
def plabel(i): return "M%d" % (i + 1) if is_monthly(i) else "Y%d" % (i - N_MONTHLY + 3)
def pyear(i): return (i // 12) + 1 if is_monthly(i) else (i - N_MONTHLY + 3)
def cal_month(i): return (i % 12) + 1 if is_monthly(i) else 0
def n_months(i): return 1 if is_monthly(i) else 12
def is_fy_end(i): return (not is_monthly(i)) or ((i + 1) % 12 == 0)


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
NAMED = []


def declare(nm, sheet, addr):
    NAMED.append((nm, "'%s'!%s" % (sheet, addr) if " " in sheet else "%s!%s" % (sheet, addr)))


def section(ws, row, text, span=8):
    for c in range(1, span + 1):
        ws.cell(row=row, column=c).fill = SECTION_FILL
    cell = ws.cell(row=row, column=1)
    cell.value, cell.font = text, SECTION_FONT
    ws.row_dimensions[row].height = 18
    return row


def banner(ws, row, text, span=31):
    for c in range(1, span + 1):
        ws.cell(row=row, column=c).fill = BANNER_FILL
    cell = ws.cell(row=row, column=1)
    cell.value, cell.font = text, BANNER_FONT
    return row


def headers(ws, row, cols):
    for col, h in cols:
        c = ws["%s%d" % (col, row)]
        c.value, c.fill, c.font, c.border = h, HEADER_FILL, HEADER_FONT, BORDER
    return row


def note(ws, row, text, col="A"):
    c = ws["%s%d" % (col, row)]
    c.value, c.font = text, NOTE_FONT


def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w


# ============================================================================
wb = Workbook()
ws_cover = wb.active
ws_cover.title = "Cover"
ws_assum = wb.create_sheet("Assumptions")
ws_scen = wb.create_sheet("Scenario Parameters")
ws_model = wb.create_sheet("Model")
ws_summ = wb.create_sheet("Summary")
for s in wb.worksheets:
    s.sheet_view.showGridLines = False

# ============================================================================
# COVER
# ============================================================================
ws_cover["B2"] = "Aurumix Revenue Model"
ws_cover["B2"].font = COVER_TITLE
ws_cover["B3"] = "Hybrid Monthly + Annual View  |  7-Year Projection"
ws_cover["B3"].font = COVER_SUB
for r, (lbl, val) in enumerate([
    ("Date", "=TODAY()"),
    ("Scope", "REVENUE ONLY. Six revenue streams, reported net of cost of revenue. Operating costs, tax, "
              "cash and funding are added in a later build."),
    ("Periods", "24 monthly (M1-M24) + 5 annual (Y3-Y7) = 29 total.  M1 = January %d" % START_YEAR),
    ("Engine", "Rolling customer balance: opening + new - churned = closing, by region. Customers who stop "
               "paying keep their gold and move to a HOLDERS balance."),
    ("Metal", "100 g bars throughout. One entry fee, one fabrication premium."),
    ("Prepared by", "Tokenomics.net: Custom Data Room Engagement"),
], start=5):
    ws_cover["B%d" % r] = lbl
    ws_cover["B%d" % r].font = BLACK_BOLD
    ws_cover["C%d" % r] = val
ws_cover["C5"].number_format = "mmmm yyyy"

ws_cover["B12"] = "COLOR LEGEND"
ws_cover["B12"].font = BLACK_BOLD
for r, (t, d, f) in enumerate([("BLUE text", "Hardcoded inputs (Assumptions & Scenario Parameters)", BLUE),
                               ("BLACK text", "In-sheet formulas", BLACK),
                               ("GREEN text", "Cross-sheet references", GREEN)], start=13):
    ws_cover["B%d" % r] = t
    ws_cover["B%d" % r].font = f
    ws_cover["C%d" % r] = d

ws_cover["B17"] = "SHEETS"
ws_cover["B17"].font = BLACK_BOLD
for r, t in enumerate([
    "Cover: This page",
    "Assumptions: Fixed inputs, activation calendar, seasonality, market ceilings",
    "Scenario Parameters: Base / Aggressive / Conservative, plus structural switches",
    "Model: Customer engine, AUM and the six revenue streams (29 periods)",
    "Summary: Annual revenue by stream (Y1-Y7), revenue mix, key metrics",
], start=18):
    ws_cover["B%d" % r] = t

ws_cover["B24"] = "SIMPLIFIED BUILD - cohort and archetype detail moves to the Phase 5 simulation."
ws_cover["B24"].font = RED_BOLD
ws_cover["B25"] = ("Kept as inputs rather than engines: card eligibility (% who qualify, months to qualify), "
                   "the holders balance, and the fabrication premium inside stream 1.")
ws_cover["B25"].font = NOTE_FONT
widths(ws_cover, {"A": 3, "B": 30, "C": 104})

# ============================================================================
# ASSUMPTIONS
# ============================================================================
ws_assum["A1"] = "=Cover!$B$2"
ws_assum["A1"].font = SHEET_TITLE
ws_assum["A2"] = "Inputs and Assumptions"
ws_assum["A2"].font = SHEET_SUB
widths(ws_assum, {"A": 54, "B": 16, "C": 24, "D": 120})
AROW, _ar = {}, [4]


def a_section(t):
    r = _ar[0]
    section(ws_assum, r, t, span=4)
    headers(ws_assum, r + 1, [("A", "Parameter"), ("B", "Value"), ("C", "Unit"), ("D", "Source")])
    _ar[0] = r + 2
    return r


def a_row(key, param, value, unit, source, fmt=FMT_NUM2, name=None):
    r = _ar[0]
    ws_assum["A%d" % r] = param
    c = ws_assum["B%d" % r]
    if value is None:
        c.value, c.font = UNFILLED, RED_BOLD
    else:
        c.value, c.font = value, BLUE
        if fmt and not isinstance(value, str):
            c.number_format = fmt
    ws_assum["C%d" % r] = unit
    ws_assum["D%d" % r] = source
    AROW[key] = r
    if name:
        declare(name, "Assumptions", "$B$%d" % r)
    _ar[0] = r + 1
    return r


def aref(k): return "Assumptions!$B$%d" % AROW[k]


a_section("PRICING AND METAL")
a_row("gold_price", "Gold price (flat)", 141.46, "USD/g",
      "USD 4,400/oz verified 2026-08-17. HELD FLAT BY DESIGN so every revenue change is attributable to the "
      "business, not the metal. CITED.", FMT_NUM2, "gold_price")
a_row("aed_usd", "AED/USD peg", 3.6725, "AED/USD", "CBUAE peg. CITED.", FMT_NUM2, "aed_usd")
a_row("entry_fee", "Entry fee charged", 0.050, "% of contribution",
      "Decision 9, client-stated. A SINGLE RATE throughout. CLIENT INPUT.", FMT_PCT2, "entry_fee")
a_row("fab_premium", "Fabrication premium paid", 0.01500, "% over spot",
      "100 g bars. OBSERVED (D28): goldtrade.ae 19 Aug 2026 measured 100 g at +1.71% (PAMP 1.75, Valcambi "
      "1.67), less the published 25 bp bulk gradient. THE ENTRY FEE IS A MARGIN, NOT A FEE - this is netted "
      "off stream 1, because it is cost OF REVENUE. Reporting stream 1 gross would read ~43% high.",
      FMT_PCT2, "fab_premium")
a_row("bar_grams", "Bar denomination", 100, "grams", "100 g throughout, by agreement. OBSERVED.",
      FMT_NUM, "bar_grams")
_ar[0] += 1

a_section("CARD ECONOMICS")
a_row("ic_gold", "Interchange - Gold", 0.01800, "% of spend",
      "Visa UAE IRF schedule, 18 Oct 2025. CITED, PRIMARY. The live model reads the FLAT GOLD RATE: replacing "
      "the full 1.80/2.05/2.10 ladder with it moves stream 2 by only ~2% of gross profit at Y7, because "
      "Sovereign is 1.2% of tiered accounts.", FMT_PCT2, "ic_gold")
a_row("txn_fee", "Per-transaction processor fee", 0.10, "USD/authorised txn",
      "WHAT THE PROCESSOR CHARGES AURUMIX to authorise and switch each transaction - NOT passed to the "
      "cardholder, and it cannot be: no consumer card charges per swipe on normal purchases, the card here is "
      "a REWARD for saving rather than a product sold, and a declined authorisation cannot be billed to "
      "anyone. Issuing economics are structurally: earn interchange, pay scheme and processing costs out of "
      "it. USD 0.10 is Stripe Issuing's PUBLISHED RACK RATE, used as a proxy because NO UAE PROCESSOR "
      "PUBLISHES PRICING. At volume, processors commonly reach USD 0.02-0.05 - a term-sheet negotiation, and "
      "at USD 0.03 the minimum profitable transaction falls from ~AED 77 to ~AED 23. CITED as a proxy.",
      FMT_USD2, "txn_fee")
a_row("decline_uplift", "Decline uplift on authorised txns", 0.06, "% uplift",
      "The processor fee is charged per AUTHORISATION, not per settled transaction, so declined attempts are "
      "billable to Aurumix and chargeable to nobody. ASSUMPTION.", FMT_PCT, "decline_uplift")
a_row("fx_margin", "FX margin on foreign spend", 0.020, "% of foreign spend",
      "Market rate ~2%, converged across four comparables. CITED.", FMT_PCT2, "fx_margin")
a_row("atm_allowance", "Free ATM allowance (Gold)", 1000, "AED/month",
      "Monthly and NOT rolling. Set deliberately ABOVE the median draw - that is the finding. CITED.",
      FMT_NUM, "atm_allowance")
a_row("atm_fee", "ATM fee over the allowance", 0.020, "% of the excess",
      "Sector converged. CITED.", FMT_PCT2, "atm_fee")
a_row("issuance_fee", "Card issuance fee", 75, "AED one-off",
      "Charged at base level, waived at upper tiers. CITED structure, ASSUMPTION rate.", FMT_NUM, "issuance_fee")
a_row("replacement_fee", "Card replacement fee", 100, "AED per event",
      "Market-normal UAE replacement is AED 75-150. ASSUMPTION.", FMT_NUM, "replacement_fee")
_ar[0] += 1

a_section("OTHER STREAM PRICING")
a_row("family_price", "Family plan / Digital Will price", 120, "USD/yr",
      "Price is ours; the cost floor is verified. ASSUMPTION.", FMT_USD, "family_price")
a_row("b2b_fee", "B2B platform fee", 0.00625, "% of partner AUM/yr",
      "Placeholder in the 0.5-0.75% band, coupled to the partner set. ASSUMPTION.", FMT_PCT2, "b2b_fee")
a_row("origination_gross", "Credit origination fee - gross", 0.0100, "% of draw",
      "Finance House UAE gold loan Key Facts Statement carries a 1% processing fee - the one gross rate with a "
      "real UAE anchor. CITED.", FMT_PCT2, "origination_gross")
a_row("origination_share", "Credit origination - Aurumix share", 0.50, "% of gross", "ASSUMPTION.",
      FMT_PCT, "origination_share")
a_row("servicing_gross", "Credit servicing fee - gross", 0.0050, "%/yr of drawn",
      "ASSUMPTION.", FMT_PCT2, "servicing_gross")
a_row("servicing_share", "Credit servicing - Aurumix share", 0.70, "% of gross",
      "The highest of the heads: servicing is where Aurumix does the actual work. ASSUMPTION.",
      FMT_PCT, "servicing_share")
a_row("ltv_gold", "LTV against collateral", 0.50, "% of collateral",
      "_draft_ics-scoring.md sec 6.2, settled 2026-08-13. CITED.", FMT_PCT, "ltv_gold")
# Spot is regionalised the same way SIP is. The multipliers are the regional SIP
# tickets divided by the book-weighted average ticket, because both are proxies
# for the SAME person's income - so a region that saves more per month also buys
# a larger one-off ticket. Normalised to average 1.00 at the base region mix, so
# the "average spot ticket" scenario parameter means exactly what it says.
for key, mult in (("uae", 1.07), ("gulf", 0.83), ("india", 0.95)):
    a_row("spotmult_" + key, "Spot ticket multiplier - %s" % RLAB[key], mult, "x average",
          "Derived from the regional SIP ticket relative to the book-weighted average of ~USD 31.5. Weighted "
          "across the region mix these average 1.00, so they redistribute the spot ticket without changing "
          "its level. DERIVED.", FMT_NUM2, "spotmult_" + key)
_ar[0] += 1

a_section("SIP RULES")
a_row("sip_floor", "SIP hard floor", 20, "USD/month",
      "Rejected outright below; never partially credited. CITED.", FMT_USD2, "sip_floor")
a_row("gate_run", "Confirmed SIP gate", 6, "consecutive payments",
      "Client's own figure. The gate is why eligibility is NOT universal - see the two eligibility parameters "
      "on the Scenario sheet. CLIENT INPUT.", FMT_NUM, "gate_run")
a_row("redemption_cost", "Cost per redemption event (memo - for the cost build)", 3.20, "USD",
      "RE-CUT 2026-08-20 from 4.20: the outbound bank transfer fee (USD 1.00-2.50) is REMOVED - that is the "
      "customer's cost to bear, not Aurumix's. What remains is Sumsub AML re-screening at 1.85 plus "
      "operational handling at ~1.35, both of which Aurumix genuinely pays. ⚠ NOT IN THE REVENUE MODEL: "
      "redemption is a COST and arrives with the cost build. This row is carried so the driver is documented "
      "and the unit rate already agreed. THE FINDING IT CARRIES IS UNCHANGED AND IS THE POINT - VARA Annex 2 "
      "III.E.4 forbids charging ANY fee on redemption, verified verbatim at primary source, so the cost is "
      "100% absorbed, no offsetting revenue exists or can exist, and THERE CAN NEVER BE AN EXIT FEE. DERIVED.",
      FMT_USD2, "redemption_cost")
_ar[0] += 1

# ----------------------------------------------------- activation calendar --
a_section("ACTIVATION CALENDAR - the single source of every activation period")
ACTIVATIONS = [
    ("s1a", 1, "from", "Stream 1a - Entry fee margin, SIP",
     "M1. The core product - live at launch."),
    ("s1b", 1, "from", "Stream 1b - Entry fee margin, SPOT",
     "M1. A sub-stream of 1: the same fee on the same gold through a different rail, so it needs no "
     "additional build."),
    ("s0", 1, "from", "Stream 0 - Redemption cost",
     "M1. A mandatory cost from day one. VARA Annex 2 III.E.4 forbids charging any fee on redemption, so "
     "there is no offsetting revenue and there can never be an exit fee."),
    ("s3", 7, "from", "Stream 3 - Family plan and Digital Will",
     "M7 (client decision 2026-08-20). RATIONALE: this is a paid add-on sold INTO an existing base, not an "
     "acquisition product. At M1 there is no base to attach it to, and the Digital Will needs the legal "
     "template and beneficiary flow finished. Six months lets the first cohort establish before they are "
     "asked to buy a second product."),
    ("s2", 13, "from", "Stream 2 - Card interchange",
     "M13 (client decision 2026-08-20, moved earlier from M18). RATIONALE FOR ANY DELAY AT ALL: the card is "
     "not ours to launch. It needs a sponsor bank (BIN sponsorship), Visa scheme certification and a "
     "processor integration - all commercial gates outside our control. It also needs customers who have "
     "cleared the six-payment gate, which takes ~8 months on average, so a card launched much earlier would "
     "have almost nobody eligible to hold it."),
    ("s4", 13, "from", "Stream 4 - Cardholder fees",
     "M13, necessarily with stream 2 - FX, ATM and issuance fees cannot exist before the card does."),
    ("s5", 13, "from", "Stream 5 - Lending revenue share",
     "M13 (client decision 2026-08-20, moved earlier from Y3). RATIONALE FOR ANY DELAY AT ALL: lending needs "
     "a partner lender under contract, and it needs collateral that has SEASONED 90 days. A customer joining "
     "at M1 has enough seasoned gold by M13; one joining at M10 does not, which the model handles because "
     "borrowers are drawn from the gate-cleared population, not from everyone."),
    ("s6", 13, "from", "Stream 6 - B2B platform fee",
     "M13 (client decision 2026-08-20, moved earlier from Y3). RATIONALE FOR ANY DELAY AT ALL: it needs a "
     "signed partner and multi-tenant capability at register and mint. NOTE: at Y3 this stream had to be "
     "placed at the START of the annual block to avoid a one-twelfth-year stub column sitting beside a full "
     "annual one. At M13 it sits safely inside the monthly block, so that complication disappears."),
    ("referral", 13, "from", "Referral channel begins",
     "M13, and this one is STRUCTURAL rather than commercial: a referrer must clear their own six-payment "
     "gate before they can refer, and the referee must then clear theirs. Two six-month gates IN SERIES. "
     "Year 1 pays nothing and the channel does not reach steady state until roughly M25."),
    ("gulf", 13, "from", "Region opens - Oman and Bahrain",
     "M13 (client decision 2026-08-20). THE ONLY STAGED REGION, and the reason is regulatory: it requires "
     "local authorisation in a second and third jurisdiction. These customers are also NOT UAE-resident, so "
     "the VAT and reporting treatment differs."),
    ("india", 1, "from", "Region opens - India",
     "M1 (client decision 2026-08-20, moved earlier from M13). The India payment route is ASSUMED SOLVED in "
     "this model. ⚠ That is a live assumption, not a settled fact - if the route is not solved, this region "
     "does not open at all and roughly a quarter of terminal revenue goes with it."),
]
for key, per, kind, label, src in ACTIVATIONS:
    a_row("act_" + key, label, per, "period # (%s)" % kind, src, FMT_NUM, "act_" + key)
_ar[0] += 1

# ---------------------------------------------------------- seasonality -----
SEAS_HDR = _ar[0]
section(ws_assum, SEAS_HDR, "SEASONALITY VECTORS (raw - the Model normalises to exactly 12.000)", span=4)
SEAS_COL0 = 6
for k, mn in enumerate(MONTHS):
    c = ws_assum.cell(row=SEAS_HDR + 1, column=SEAS_COL0 + k)
    c.value, c.fill, c.font = mn, HEADER_FILL, HEADER_FONT
    c.alignment = Alignment(horizontal="center")
    ws_assum.column_dimensions[get_column_letter(SEAS_COL0 + k)].width = 8
ws_assum["A%d" % (SEAS_HDR + 1)] = "Vector"
_ar[0] = SEAS_HDR + 2
SEAS_ROW = {}
for key, label, vals, src in [
    ("acq", "Acquisition seasonality",
     [1.01, 0.96, 0.92, 1.15, 1.04, 0.88, 0.85, 0.85, 0.93, 1.25, 1.15, 1.01],
     "SOURCED TIMING, JUDGED AMPLITUDE. Peaks at Akshaya Tritiya (Apr/May), the most concentrated gold-buying "
     "day globally by value, and Dhanteras/Diwali (Oct/Nov), India's peak gold occasion with demand up 8-12% "
     "in the fortnight before. Wedding season Nov-Mar supports the winter. Trough Jul-Sep, the sourced annual "
     "low. Jan carries the Dubai Shopping Festival. DAMPED to ~+/-25% against the ~+/-33% swing in raw "
     "jewellery demand, because a USD 20/month savings mandate is far less impulsive than buying jewellery. "
     "Two traps avoided: India's Q3 2024 spike was an IMPORT DUTY CUT, not seasonality; and Ramadan/Eid moves "
     "~11 days a year, so a fixed-month Eid bump would be wrong by construction over 7 years."),
    ("spend", "Card spend seasonality",
     [1.10, 1.00, 0.98, 0.98, 1.00, 0.95, 0.88, 0.90, 1.00, 1.02, 1.05, 1.14],
     "UAE RESIDENT CARD SPEND, not gold. Peaks Dec-Jan on the Dubai Shopping Festival and year-end holidays; "
     "troughs Jul-Aug when residents leave for the summer. NARROWER than acquisition (+/-14% vs +/-25%) "
     "because everyday spend is less culturally spiky. Note the deliberate OPPOSITION to the foreign-spend "
     "vector: Jul-Aug is the weakest total-spend month and the strongest foreign-share month."),
    ("foreign", "Foreign-spend share vector",
     [30, 30, 30, 32, 34, 55, 60, 56, 36, 42, 40, 32],
     "The one seasonality vector the brief itself tabulates. Raw mean 39.75, rescaled on the Model to the "
     "foreign-spend-share parameter. THE SUMMER TRAVEL SEASON IS THE LARGEST STREAM-4 MONTH on the weakest "
     "total-spend base."),
]:
    r = _ar[0]
    ws_assum["A%d" % r] = label
    for k, v in enumerate(vals):
        c = ws_assum.cell(row=r, column=SEAS_COL0 + k)
        c.value, c.font, c.number_format = v, BLUE, FMT_NUM2
        c.alignment = Alignment(horizontal="center")
    ws_assum["D%d" % r] = src
    SEAS_ROW[key] = r
    _ar[0] += 1
_ar[0] += 1

# ------------------------------------------------------ market ceilings -----
a_section("REGION KEY - who each region is")
for key in REGIONS:
    r = _ar[0]
    ws_assum["A%d" % r] = RLAB[key]
    ws_assum["A%d" % r].font = BLACK_BOLD
    # R1 carries no activation row: it is the baseline market, open from M1 by
    # definition, and the region renormalisation treats it as always open.
    _opens = dict((k, p) for k, p, _a, _b, _c in ACTIVATIONS).get(key, 1)
    ws_assum["B%d" % r] = "opens M%d" % _opens
    ws_assum["B%d" % r].font = SECONDARY
    ws_assum["D%d" % r] = RDESC[key]
    _ar[0] += 1
_ar[0] += 1

# ---------------------------------------------------------------------------
# MARKET SIZING - the funnel, shown as live arithmetic rather than a typed
# ceiling. Four source populations feed three model regions; every step is a
# visible cell, so a reader can see exactly how 12.5m people become 43,750
# reachable accounts and can argue with any single filter.
# ---------------------------------------------------------------------------
FUN_HDR = _ar[0]
section(ws_assum, FUN_HDR, "MARKET SIZING - how each region's reachable SIP account ceiling is derived", span=4)
FUN0 = 6                                    # column F
FUNNEL = [
    ("uae_ind", "UAE - Indian", 4360000, 0.80, 0.57, 0.40, 0.095, "uae"),
    ("uae_osa", "UAE - other South Asian", 3460000, 0.80, 0.57, 0.40, 0.060, "uae"),
    ("gulf", "Oman and Bahrain", 2630000, 1.00, 0.57, 0.40, 0.040, "gulf"),
    ("india", "India", 12500000, 1.00, 1.00, 1.00, 0.0035, "india"),
]
for k, (key, nm, pop, ea, pay, mon, ceil, rgn) in enumerate(FUNNEL):
    c = ws_assum.cell(row=FUN_HDR + 1, column=FUN0 + k)
    c.value, c.fill, c.font = nm, HEADER_FILL, HEADER_FONT
    c.alignment = Alignment(horizontal="center", wrap_text=True)
    ws_assum.column_dimensions[get_column_letter(FUN0 + k)].width = 15
ws_assum["A%d" % (FUN_HDR + 1)] = "Funnel step"
ws_assum["A%d" % (FUN_HDR + 1)].fill = HEADER_FILL
ws_assum["A%d" % (FUN_HDR + 1)].font = HEADER_FONT
_ar[0] = FUN_HDR + 2

FUN_ROW = {}


def fun_row(key, label, vals, fmt, src, font=BLUE):
    r = _ar[0]
    ws_assum["A%d" % r] = label
    for k, v in enumerate(vals):
        c = ws_assum.cell(row=r, column=FUN0 + k)
        c.value = v
        c.font = font
        c.number_format = fmt
        c.alignment = Alignment(horizontal="center")
    ws_assum["D%d" % r] = src
    FUN_ROW[key] = r
    _ar[0] += 1
    return r


fun_row("pop", "Source population", [f[2] for f in FUNNEL], FMT_NUM,
        "UPDATED 2026-08-20. UAE-Indian is 4.36m - the Indian consulate's official count at December 2024, "
        "also given as 4.3m by the Embassy of India. The brief carried 3.5m, which is roughly a 2021-22 "
        "vintage: the community was 3.89m at December 2023 and 4.36m a year later, having doubled from 2.2m "
        "over the decade. UAE-other South Asian is 3.46m, the sum of Pakistani 1.90m, Bangladeshi 0.84m, "
        "Nepali 0.36m and Sri Lankan 0.36m - the brief's 3.4m was already correct. These are TOTAL RESIDENT "
        "NATIONALS including dependants, which is why the economically-active filter below applies. Oman and "
        "Bahrain is an expatriate WORKER count. INDIA IS NOT A DEMOGRAPHIC BASE - it is sized BEHAVIOURALLY "
        "from gold ETF folios intersected with active digital-gold holders, so its filters are 100%. "
        "⚠ HELD STATIC over the horizon, which is conservative: the UAE Indian community grew ~12% in the "
        "single year to Dec 2024.")
fun_row("ea", "  x Economically active", [f[3] for f in FUNNEL], FMT_PCT,
        "Oman and Bahrain is 100% because the source counts EXPAT WORKERS, who are working-age and "
        "economically active by definition - applying a labour-force filter would double-count.")
fun_row("pay", "  x Payment capable (IBAN able to carry a direct debit)", [f[4] for f in FUNNEL], FMT_PCT,
        "A SIP needs a standing mandate, not just an account. This is the filter that replaced an unsourced "
        "gold-savings propensity filter, which was flagged as the weakest link in the entire sizing and had "
        "no published source. This one has a stated mechanism behind it.")
fun_row("mon", "  x Money capable (USD 20/month after remittances)", [f[5] for f in FUNNEL], FMT_PCT,
        "Discretionary capacity for a RECURRING USD 240/year commitment, tested after remittance obligations "
        "rather than before them.")
_ab = _ar[0]
fun_row("addr", "  = Addressable base", [None] * 4, FMT_NUM,
        "Population x the three filters. The UAE-Indian column reproduces the brief's worked figure of "
        "~640,000.", BLACK_BOLD)
for k in range(4):
    col = get_column_letter(FUN0 + k)
    c = ws_assum["%s%d" % (col, _ab)]
    c.value = "=%s%d*%s%d*%s%d*%s%d" % (col, FUN_ROW["pop"], col, FUN_ROW["ea"],
                                        col, FUN_ROW["pay"], col, FUN_ROW["mon"])
    c.font, c.number_format = BLACK_BOLD, FMT_NUM
    c.alignment = Alignment(horizontal="center")
fun_row("ceilpct", "  x Penetration ceiling", [f[6] for f in FUNNEL], FMT_PCT2,
        "The share of the addressable base the product could ever reach. 'base x ceiling' is the INVARIANT - "
        "changing one without the other silently re-scales the whole model.")
_rc = _ar[0]
fun_row("acct", "  = REACHABLE SIP ACCOUNTS", [None] * 4, FMT_NUM,
        "This is what the acquisition engine saturates against.", BLACK_BOLD)
for k in range(4):
    col = get_column_letter(FUN0 + k)
    c = ws_assum["%s%d" % (col, _rc)]
    c.value = "=%s%d*%s%d" % (col, _ab, col, FUN_ROW["ceilpct"])
    c.font, c.number_format = BLACK_BOLD, FMT_NUM
    c.alignment = Alignment(horizontal="center")
r = _ar[0]
ws_assum["A%d" % r] = "  Feeds model region"
for k, f in enumerate(FUNNEL):
    c = ws_assum.cell(row=r, column=FUN0 + k)
    c.value = RLAB[f[7]]
    c.font = SECONDARY
    c.alignment = Alignment(horizontal="center")
_ar[0] += 2

a_section("MARKET CEILINGS AND ACQUISITION DRIVERS")
for key in REGIONS:
    cols = [get_column_letter(FUN0 + k) for k, f in enumerate(FUNNEL) if f[7] == key]
    src = ("DERIVED from the market sizing funnel above - the sum of its source populations (%s), not a typed "
           "number. Change any filter and this follows."
           % ", ".join(FUNNEL[k][1] for k, f in enumerate(FUNNEL) if f[7] == key))
    r = _ar[0]
    ws_assum["A%d" % r] = "Reachable SIP ceiling - %s" % RLAB[key]
    c = ws_assum["B%d" % r]
    c.value = "=" + "+".join("%s%d" % (cl, _rc) for cl in cols)
    c.font, c.number_format = BLACK_BOLD, FMT_NUM
    ws_assum["C%d" % r] = "accounts"
    ws_assum["D%d" % r] = src
    AROW["ceil_" + key] = r
    declare("ceil_" + key, "Assumptions", "$B$%d" % r)
    _ar[0] += 1
r = _ar[0]
ws_assum["A%d" % r] = "Total reachable SIP accounts"
ws_assum["A%d" % r].font = BLACK_BOLD
ws_assum["B%d" % r] = "=" + "+".join(aref("ceil_" + k).replace("Assumptions!", "") for k in REGIONS)
ws_assum["B%d" % r].font = BLACK_BOLD
ws_assum["B%d" % r].number_format = FMT_NUM
ws_assum["C%d" % r] = "accounts"
ws_assum["D%d" % r] = ("~181,150, against the brief's 165,750. ⚠ THE BRIEF'S 'base x ceiling is the "
                       "invariant' RULE IS DELIBERATELY BROKEN HERE, and the distinction matters: that rule "
                       "guards against a METHODOLOGICAL re-cut quietly inflating the market by re-tuning "
                       "filters, which proves nothing. This is not that - it is a DATA CORRECTION. The UAE "
                       "Indian population really is 4.36m rather than 3.5m, so the addressable market really "
                       "is larger. Holding the invariant would mean asserting that penetration falls exactly "
                       "as population rises, which has no basis. The penetration ceilings are untouched.")
AROW["ceil_total"] = r
declare("ceil_total", "Assumptions", "$B$%d" % r)
_ar[0] += 1
AGENTS = [5, 15, 40, 60, 90, 106, 124]
MKTG = [60000, 180000, 250000, 400000, 600000, 850000, 1100000]
RAMP = [0.60, 0.85, 1.00, 1.00, 1.00, 1.00, 1.00]
for y in range(1, 8):
    a_row("agents_y%d" % y, "Active agents - Y%d" % y, AGENTS[y - 1], "agents",
          "A STOCK, not a flow: at 45% attrition, holding 200 active needs ~90 recruits a year. CLIENT INPUT.",
          FMT_NUM, "agents_y%d" % y)
for y in range(1, 8):
    a_row("mktg_y%d" % y, "Marketing spend - Y%d" % y, MKTG[y - 1], "USD/yr",
          "A DECISION VARIABLE and an input to acquisition, not an output of a cost table.", FMT_USD, "mktg_y%d" % y)
for y in range(1, 8):
    a_row("ramp_y%d" % y, "Agent blended ramp - Y%d" % y, RAMP[y - 1], "x productivity",
          "Six months to full productivity, which happens to match the six-payment gate.", FMT_NUM2, "ramp_y%d" % y)
# WHERE EACH CHANNEL CAN ACTUALLY SELL. Previously every channel was allocated
# to every region in the same proportion, which quietly put agents to work in
# markets they do not operate in.
AGENT_SHARE = {"uae": 0.00, "gulf": 0.00, "india": 1.00}
for key in REGIONS:
    a_row("agentshare_" + key, "Share of agent-driven acquisition - %s" % RLAB[key],
          AGENT_SHARE[key], "% of agent output",
          "CLIENT INPUT 2026-08-20: THE AGENT NETWORK OPERATES IN INDIA ONLY. Outside India acquisition is "
          "marketing spend, referrals and organic only. ⚠ THIS CONTRADICTS THE ARCHITECTURE BRIEF, which "
          "allocates agents across every region through its channel-to-region mix and argues that the agent "
          "network is Indian and 'must recruit non-Indian agents before it reaches the other South Asian "
          "market at all' - wording that assumes agents are already selling to the UAE diaspora. The client "
          "instruction is taken as authoritative and the brief's mix is superseded. Must sum to 100%.",
          FMT_PCT, "agentshare_" + key)
_ar[0] += 1
ws_assum.freeze_panes = "B6"

# ============================================================================
# SCENARIO PARAMETERS
# ============================================================================
ws_scen["A1"] = "=Cover!$B$2"
ws_scen["A1"].font = SHEET_TITLE
ws_scen["A2"] = "Scenario Parameters"
ws_scen["A2"].font = SHEET_SUB
widths(ws_scen, {"A": 50, "B": 15, "C": 14, "D": 14, "E": 14, "F": 24, "G": 118})

section(ws_scen, 4, "SCENARIO SELECTOR", span=5)
ws_scen["A6"] = "Select Scenario:"
ws_scen["A6"].font = BLACK_BOLD
ws_scen["B6"] = "Base"
ws_scen["B6"].font = BLUE_BOLD
ws_scen["C6"] = '=IF($B$6="Base",1,IF($B$6="Aggressive",2,3))'
ws_scen["D6"] = "<- index"
ws_scen["D6"].font = SECONDARY
ws_scen["G6"] = "One switch, three columns. Every parameter below resolves through it."
ws_scen["G6"].font = NOTE_FONT
dv = DataValidation(type="list", formula1='"Base,Aggressive,Conservative"', allowBlank=False)
ws_scen.add_data_validation(dv)
dv.add(ws_scen["B6"])
declare("scenario_index", "Scenario Parameters", "$C$6")

SROW, _sr = {}, [8]
SIDX = "$C$6"
# Every scenario parameter is MIRRORED into Assumptions as a green link, and the
# Model reads only from there. Recorded here so the mirror can be generated with
# the same label, unit, format and rationale - one source in code, no drift.
SORDER, SMETA = [], {}


def s_section(t):
    r = _sr[0]
    section(ws_scen, r, t, span=5)
    headers(ws_scen, r + 1, [("A", "Parameter"), ("B", "Active Value"), ("C", "Base"),
                             ("D", "Aggressive"), ("E", "Conservative"), ("F", "Unit")])
    _sr[0] = r + 2
    return r


def sp(key, param, base, agg, cons, unit, why, fmt=FMT_NUM2, name=None):
    r = _sr[0]
    ws_scen["A%d" % r] = param
    ws_scen["B%d" % r] = "=CHOOSE(%s,C%d,D%d,E%d)" % (SIDX, r, r, r)
    ws_scen["B%d" % r].font = BLACK_BOLD
    ws_scen["B%d" % r].number_format = fmt
    for col, val in (("C", base), ("D", agg), ("E", cons)):
        c = ws_scen["%s%d" % (col, r)]
        if val is None:
            c.value, c.font = UNFILLED, RED_BOLD
        else:
            c.value, c.font, c.number_format = val, BLUE, fmt
    ws_scen["F%d" % r] = unit
    ws_scen["F%d" % r].font = SECONDARY
    ws_scen["G%d" % r] = why
    ws_scen["G%d" % r].font = NOTE_FONT
    SROW[key] = r
    SORDER.append(key)
    SMETA[key] = (param, unit, why, fmt)
    if name:
        declare(name, "Scenario Parameters", "$B$%d" % r)
    _sr[0] = r + 1
    return r


def s_derived(key, param, formula, unit, why, fmt=FMT_PCT2, name=None):
    r = _sr[0]
    ws_scen["A%d" % r] = param
    ws_scen["B%d" % r] = formula
    ws_scen["B%d" % r].font = BLACK_BOLD
    ws_scen["B%d" % r].number_format = fmt
    ws_scen["F%d" % r] = unit
    ws_scen["F%d" % r].font = SECONDARY
    ws_scen["G%d" % r] = why
    ws_scen["G%d" % r].font = NOTE_FONT
    SROW[key] = r
    SORDER.append(key)
    SMETA[key] = (param, unit, why, fmt)
    if name:
        declare(name, "Scenario Parameters", "$B$%d" % r)
    _sr[0] = r + 1
    return r


# While the Scenario sheet is being built, references point at itself. Once the
# Assumptions mirror exists this is REBOUND to point there instead, so every
# Model formula resolves through Assumptions - see the mirror block below.
def sref(k): return "'Scenario Parameters'!$B$%d" % SROW[k]


s_section("GROUP A: CUSTOMERS AND CHURN")
sp("persistency_m13", "Persistency - customers still paying after 12 months", 0.55, 0.65, 0.45, "%",
   "THE HEADLINE RETENTION NUMBER, and the one a client can argue with. Everything about churn is derived "
   "from it. Governs lifetime value, referral economics and agent commission at once. DERIVED from the "
   "archetype work: the simulation can refine it, but 55% is what that engine produced.", FMT_PCT, "persistency_m13")
s_derived("monthly_churn", "Monthly churn rate (derived)",
          "=1-%s^(1/12)" % sref("persistency_m13"), "%/month",
          "DERIVED, not typed: the monthly rate that reproduces the persistency above over twelve months. "
          "Change persistency and this follows. Base 55% implies ~4.9%/month.", FMT_PCT2, "monthly_churn")
sp("agent_productivity", "Agent productivity", 4, 6, 2, "accounts/agent/month",
   "Insurance agency comparator. TRIANGULATED.", FMT_NUM2, "agent_productivity")
CAC_BY_REGION = {"uae": (120, 80, 200), "gulf": (100, 70, 170), "india": (20, 12, 35)}
for key in REGIONS:
    b, a, c = CAC_BY_REGION[key]
    sp("cac_" + key, "Marketing CAC - %s" % RLAB[key], b, a, c, "USD per customer",
       "REGIONALISED 2026-08-20. A single global USD 120 was applied everywhere, which is roughly right for "
       "the UAE and badly wrong for India. PUBLISHED BENCHMARKS: Dubai consumer fintech USD 65-220; retail "
       "neobank account paid-only USD 35-70; GCC wealthtech funded accounts USD 80-220; 'true' fully-loaded "
       "CAC per ACTIVATED customer USD 85-350 against USD 50-100 reported, once KYC, onboarding and "
       "non-activating signups are counted. INDIA IS A DIFFERENT MARKET ENTIRELY: consumer fintech "
       "INR 500-1,500 (~USD 6-18), neobank savings activation INR 1,100-1,800, wealth and broking apps "
       "INR 2,500-5,500 (~USD 30-65); Jupiter reports a USD 5-6 paid CAC. USD 120 is ~INR 10,500 - some 7-20x "
       "the Indian mass-market benchmark and still 2-4x its premium wealth apps. UAE is held at 120 as a "
       "FULLY-LOADED figure; ⚠ note it sits at the top of the range for a LOW-TICKET product, and the "
       "published low-ticket band is USD 4-70. TRIANGULATED.", FMT_USD, "cac_" + key)
MKT_SHARE = {"uae": 0.58, "gulf": 0.16, "india": 0.26}
for key in REGIONS:
    sp("mktshare_" + key, "Marketing spend share - %s" % RLAB[key], MKT_SHARE[key], MKT_SHARE[key],
       MKT_SHARE[key], "% of budget",
       "How the marketing budget is split across markets. Defaults to each region's share of the addressable "
       "ceiling, so spend follows the opportunity. Does not vary by scenario - it is a management decision, "
       "not an uncertainty. Must sum to 100%.", FMT_PCT, "mktshare_" + key)
sp("referral_rate", "Referral rate", 0.45, 0.90, 0.18, "referrals/customer/yr",
   "Cap removed deliberately, so the distribution is right-skewed. MODEL THE MEAN, NOT THE MEDIAN. ASSUMPTION.",
   FMT_NUM2, "referral_rate")
sp("referral_conversion", "Referral conversion", 0.62, 0.72, 0.48, "%",
   "The M7 survival of the referred cohort, uplifted ~1.1x. DERIVED.", FMT_PCT, "referral_conversion")
sp("organic_share", "Organic share of direct", 0.12, 0.20, 0.05, "% of direct",
   "Kept separate so the CAC never applies to it. ASSUMPTION.", FMT_PCT, "organic_share")
sp("seasonality_amplitude", "Seasonality amplitude", 1.00, 1.40, 0.60, "x deviation from 1.0",
   "Festival TIMING is sourced; how hard a Dubai savings signup responds to Dhanteras is the open question. "
   "Applied to the deviation from 1.0, then renormalised, so the vectors stay at exactly 12.000.",
   FMT_NUM2, "seasonality_amplitude")
_sr[0] += 1

s_section("GROUP B: CARD ELIGIBILITY - the two cells that replace the archetype engine")
sp("ever_qualify", "Customers who EVER clear the six-payment gate", 0.55, 0.65, 0.45, "% of customers",
   "THE SINGLE MOST LOAD-BEARING PARAMETER IN THE MODEL. The card streams are ~83% of gross profit and every "
   "one of them requires clearing the six-payment gate. Assuming everyone qualifies - which any plain churn "
   "model does implicitly - OVERSTATES THE BUSINESS BY ~59%. Base 55% is the OUTPUT of the run-of-6 "
   "first-passage engine built and validated against the archetype mix; that engine has moved to the Phase 5 "
   "simulation, and this cell is what it produced.", FMT_PCT, "ever_qualify")
sp("months_to_qualify", "Average months to clear the gate", 8, 6, 11, "months",
   "Gate arrival is a DISTRIBUTION, not a date: a customer who misses month 4 cannot qualify before month 9. "
   "The validated mean is M8.0, against the naive assumption of M6. Those two extra months are full-fee "
   "revenue that carries no benefit cost, and they push every downstream ladder date to the right. DERIVED.",
   FMT_NUM, "months_to_qualify")
_sr[0] += 1

s_section("GROUP C: AUM, LEAKAGE AND SPOT")
sp("self_custody_leakage", "Self-custody leakage", 0.12, 0.06, 0.30, "% of AUM/yr",
   "Gold withdrawn to a customer's own wallet. Free to Aurumix but it leaves AUM. ASSUMPTION.",
   FMT_PCT, "self_custody_leakage")
sp("redemption_rate", "Redemption rate", 0.08, 0.04, 0.16, "% of AUM/yr",
   "A DIFFERENT EVENT from self-custody and a separate line. PAXG turnover of 5.9% is the only comparator. "
   "VARA forbids charging any fee on it. ASSUMPTION.", FMT_PCT, "redemption_rate")
sp("lapsed_redemption_mult", "Holder redemption multiplier", 2.2, 1.6, 3.5, "x the paying rate",
   "Customers who stopped paying redeem FASTER - they have no accruing benefit left to protect. Because "
   "holders become the majority of the book by Y4, this is the DOMINANT AUM DECAY TERM from roughly Y4. "
   "ASSUMPTION.", FMT_NUM2, "lapsed_redemption_mult")
sp("spot_attach", "Spot attach rate", 0.14, 0.24, 0.07, "% of customers/yr",
   "Load-bearing because it is MISSING, not because it is large. ASSUMPTION.", FMT_PCT, "spot_attach")
sp("spot_ticket", "Average spot ticket", 300, 530, 200, "USD/event",
   "RE-ANCHORED 2026-08-20 from USD 620. Botim - a UAE gold-buying app with a 96% blue/grey collar base, and "
   "the ONLY OBSERVED SPOT FUNNEL IN THE LAUNCH MARKET - reports an average ticket of ~AED 780 (~USD 212). "
   "USD 620 sat at 2.9x the only observed figure for this demographic, which is the same population-mismatch "
   "error corrected on card spend the same day. USD 300 stays ABOVE the observed figure, on the argument that "
   "a considered purchase into an allocated-gold savings product is larger than a casual in-app buy, but no "
   "longer multiples above it. Conservative sits at USD 200, just below Botim. Scaled by region below. "
   "ASSUMPTION anchored on one observation.", FMT_USD, "spot_ticket")
sp("spot_frequency", "Spot frequency", 1.7, 2.4, 1.2, "events/attacher/yr",
   "External check: Botim's 128,000 trades against ~45,000 buyers implies ~1.9/yr. INFERRED from two "
   "disclosures of different vintage - supportive, not confirmatory. ASSUMPTION.", FMT_NUM2, "spot_frequency")
sp("spot_to_sip", "Spot-to-SIP conversion", 0.08, 0.15, 0.03, "% of spot buyers/yr",
   "NO SOURCE EXISTS ANYWHERE - re-confirmed by search 2026-08-20, a CONFIRMED NEGATIVE rather than a gap in "
   "the searching. The mechanism design calls this arrow 'the growth funnel' and names spot 'the entry point "
   "for new investors'. THE STRATEGY QUESTION IN NUMERICAL FORM, and the one an experiment could answer.",
   FMT_PCT, "spot_to_sip")
_sr[0] += 1

s_section("GROUP D: CARD")
sp("pm_share", "Programme manager share of interchange", 0.72, 0.85, 0.55, "%",
   "SIZES THE LARGEST STREAM. No UAE/MENA figure is published. FLOOR IS 36% - take that into the sponsor "
   "conversation as the walk-away. TRIANGULATED.", FMT_PCT, "pm_share")
sp("card_activation", "Facility take-up - customers who take AND use the card", 0.18, 0.30, 0.08,
   "% of gate-cleared",
   "RE-BASED 2026-08-20, client decision: THE CARD IS A DRAWDOWN ON THE GOLD-COLLATERALISED FACILITY, not a "
   "salary-repaid revolving card. Aurumix has no balance sheet to lend from - it can only extend credit "
   "against collateral it holds, which is the customer's gold. Using the card IS borrowing, so card "
   "activation and credit take-up are the SAME behaviour and were previously modelled as two different "
   "populations (50% activating a card, 18% taking credit) doing what is in fact one thing. Merged onto the "
   "credit figure, which is the better-anchored of the two: Indian gold-loan penetration is under 10% at a "
   "point in time, uplifted here for pre-selection since these customers have already cleared a "
   "six-payment gate. ⚠ THE OLD 50% CAME FROM NEOBANK COMPARABLES (PULSE 68.2%, Monzo 68%) WHERE THE CARD "
   "IS THE PRODUCT - wrong in kind for a card that only lets you borrow against your own savings. "
   "DERIVED.", FMT_PCT, "card_activation")
sp("card_txns_per_draw", "Transactions per drawdown event", 4, 6, 2, "transactions/draw",
   "RE-BASED 2026-08-20 from 12 transactions/MONTH once the card became a drawdown on the gold facility. "
   "Under that model the customer borrows a lump (limit x drawn share) a couple of times a year and spends "
   "it down, so the meaningful unit is transactions PER DRAW, not per month. At 12/month the implied ticket "
   "collapsed to ~AED 12, which is a coffee, not a reason to pledge your gold. THE AVERAGE TICKET FALLS OUT "
   "AS drawn amount / this number, and the draw events cancel - so the ticket depends only on how large a "
   "draw is and how many purchases it is spent across. ⚠ IT ALSO CHANGES WHAT THE CARD IS FOR: not daily "
   "groceries, but occasional larger needs - school fees, a medical bill, an emergency - funded by borrowing "
   "against savings rather than liquidating them. That is a materially different product story and should be "
   "put to the client in those words. ASSUMPTION.", FMT_NUM, "card_txns_per_draw")
sp("card_txns_UNUSED", "Card transactions per active card per month", 12, 18, 8, "transactions/month",
   "THE INPUT IS FREQUENCY; AVERAGE TICKET IS DERIVED FROM IT. That inversion is deliberate. Monthly spend is "
   "already pinned by income (a multiple of the SIP ticket) and capped by the gold collateral, so specifying a "
   "ticket size would over-determine the card and let it drift away from what the customer actually saves - "
   "the exact problem an absolute AED 100 ticket created. Fixing frequency instead makes the average ticket "
   "fall out as spend / frequency, which means IT SCALES WITH THE SIP CONTRIBUTION AUTOMATICALLY: a customer "
   "on a smaller monthly savings amount gets a proportionally smaller basket, in every region, with no extra "
   "input. WHY FREQUENCY IS THE BETTER THING TO ANCHOR: it has a published number and ticket size does not. "
   "Visa scheme data gives ~175 transactions per card per year for the region, about 14-15/month, and UAE "
   "low-income cash dependency fell from 84% to 69% in two years, so card usage is rising. Base is set at 12, "
   "slightly BELOW the general anchor, because this is a secondary card earned on a savings product rather "
   "than someone's main salary card. ⚠ THE UAE-WIDE AVERAGE TICKET OF ~AED 313 IS DELIBERATELY NOT USED - it "
   "spans affluent expats and corporate cards, which is the same population mismatch that put card spend at "
   "AED 6,000. NO PUBLISHED TICKET SIZE OR FREQUENCY EXISTS FOR BLUE-COLLAR GCC WORKERS SPECIFICALLY - a "
   "confirmed negative, re-checked 2026-08-20. TRIANGULATED on frequency, DERIVED on ticket.",
   FMT_NUM, "card_txns_per_month")
sp("foreign_spend_share", "Foreign spend share (mean)", 0.34, 0.45, 0.24, "% of card spend",
   "Applied through the seasonal vector, not as a constant. ASSUMPTION.", FMT_PCT, "foreign_spend_share")
sp("issuance_events", "Card issuance events", 1.06, 1.04, 1.10, "events/card/yr",
   "1.00 at activation plus reissues - a tier upgrade forces a physical reissue. ASSUMPTION.",
   FMT_NUM2, "issuance_events")
sp("replacement_events", "Card replacement events", 0.11, 0.07, 0.18, "events/card/yr",
   "Industry-normal loss/theft/damage is 8-15% annually. ASSUMPTION.", FMT_NUM2, "replacement_events")
ATM = [("a500", "AED 0-500", 0.60, 0.42, 0.74, 250, 300, 200),
       ("a1500", "AED 500-1,500", 0.25, 0.30, 0.18, 1000, 1100, 900),
       ("a3000", "AED 1,500-3,000", 0.12, 0.20, 0.06, 2250, 2400, 2100),
       ("a3000p", "AED 3,000+", 0.03, 0.08, 0.02, 4000, 4500, 3600)]
for key, nm, b, a, c, mb, ma, mc in ATM:
    sp("atm_" + key, "ATM %s - share of cardholders" % nm, b, a, c, "%",
       "KEPT AS A DISTRIBUTION DELIBERATELY. The mean draw (~AED 940) sits just BELOW the free allowance of "
       "AED 1,000 BY DESIGN, so applying the fee to the mean returns EXACTLY ZERO and stream 4 silently loses "
       "a component. The distribution returns materially more, generated almost entirely by a small high-cash "
       "tail. ASSUMPTION.", FMT_PCT, "atm_" + key)
for key, nm, b, a, c, mb, ma, mc in ATM:
    sp("atmm_" + key, "ATM %s - midpoint draw" % nm, mb, ma, mc, "AED/month",
       "Raising the allowance at the top tier waives revenue from only the top ~3% of cardholders.",
       FMT_NUM, "atmm_" + key)
_sr[0] += 1

s_section("GROUP E: CREDIT, B2B AND FAMILY")
# Credit take-up is GONE - merged into facility take-up in Group D, because
# under the gold-drawdown model taking a card and taking credit are one act.
sp("drawn_share", "Drawn as % of permitted limit", 0.50, 0.70, 0.30, "%",
   "Revolving facilities draw 40-55% of permitted. This now drives CARD SPEND as well as the loan balance, "
   "because the card is the drawdown mechanism. TRIANGULATED.", FMT_PCT, "drawn_share")
sp("facility_turnover", "Facility turnover, peak -> average", 0.42, 0.55, 0.30, "x peak drawn",
   "AN ARITHMETIC CORRECTION, not a sensitivity, derived from Manappuram's 71-day realised tenor. It cuts "
   "the lending stream by 1.88x. DERIVED.", FMT_NUM2, "facility_turnover")
sp("draw_events", "Draw events per borrower per year", 2.1, 3.2, 1.3, "events/yr",
   "MOVES WITH facility turnover - do not flex independently. DERIVED.", FMT_NUM2, "draw_events")
sp("family_attach", "Family plan attach rate", 0.20, 0.35, 0.10, "% of customers",
   "NOTHING IS STATED ANYWHERE IN THE CORPUS. Pure assumption. Scales stream 3 linearly.", FMT_PCT, "family_attach")
for y in range(1, 8):
    b, a, c = ([0, 1, 2, 3, 4, 5, 6][y - 1], [0, 1, 3, 5, 7, 9, 11][y - 1], [0, 1, 1, 1, 2, 2, 2][y - 1])
    sp("partners_y%d" % y, "B2B partners - Y%d" % y, b, a, c, "partners",
       "Enterprise cadence for a pre-revenue infrastructure vendor. Partner 1 signs in Y2, matching the M13 "
       "B2B go-live - the schedule previously started at Y3 and had to move with it, or stream 6 would have "
       "activated with no partner to earn on. TERMINAL COUNTS ARE UNCHANGED, so the pipeline accelerates by "
       "a year without inflating the addressable partner market. ASSUMPTION.",
       FMT_NUM, "partners_y%d" % y)
sp("aum_per_partner", "AUM per partner (mature)", 32000000, 45000000, 22000000, "USD",
   "Requires a signed partner. Partner AUM earns NO tier and consumes NO benefits - structurally the "
   "highest-margin book. DERIVED.", FMT_USD, "aum_per_partner")
_sr[0] += 1

s_section("GROUP F: REGIONS")
RDATA = [("uae", 33.6, 41.0, 26.5, 0), ("gulf", 26, 32, 21, 0), ("india", 30, 36, 24, 0)]
for key, tb, ta, tc, mix in RDATA:
    sp("ticket_" + key, "Average monthly ticket - %s" % RLAB[key], tb, ta, tc, "USD/month",
       "THE SIP AMOUNT - the recurring monthly gold contribution. SAVINGS-CAPACITY anchored, not remittance "
       "anchored, because remittance is a committed obligation rather than discretionary money; a recurring "
       "gold debit realistically captures 10-15% of monthly savings capacity. Anchors: Joyalukkas has "
       "PRICE-DISCOVERED AED 100 (USD 27) as the viable mass-market monthly instalment for this exact "
       "demographic, and Malabar sits at AED 200. The blend lands BELOW AMFI's USD 34 Indian retail SIP "
       "average (Rs 31,961 crore over 10.63 crore accounts, current at July 2026), which is the correct "
       "direction since AMFI reflects domestic urban investors with more discretionary income than a Gulf "
       "blue-collar book - it is an upper bound, not a proxy. UAE is the ceiling-weighted blend of the former "
       "Indian (USD 38) and other South Asian (USD 26) rows. Book-weighted average ~USD 31.45. TRIANGULATED.",
       FMT_USD, "ticket_" + key)
for key, tb, ta, tc, mix in RDATA:
    s_derived("mix_" + key, "Share of new customers - %s" % RLAB[key],
              "=%s/(%s)" % (aref("ceil_" + key), "+".join(aref("ceil_" + k) for k in REGIONS)),
              "% of new",
              "DERIVED from market size: each region's share of acquisition equals its share of the "
              "addressable ceiling, so acquisition follows the opportunity. Previously these were four typed "
              "numbers with no basis, which sent 34% of acquisition to Oman and Bahrain - a market that is "
              "16% of the opportunity - and only 8% to India, which is 26% of it. Because they are derived "
              "they sum to 1.000 by construction and cannot drift out of line with the ceilings. Shares are "
              "RENORMALISED on the Model for regions not yet open, so a region that opens later redistributes "
              "rather than vanishing.", FMT_PCT, "mix_" + key)
_sr[0] += 1

section(ws_scen, _sr[0], "STRUCTURAL SWITCHES - the two that move revenue", span=5)
headers(ws_scen, _sr[0] + 1, [("A", "Switch"), ("B", "Active (1/0)"), ("C", "State"), ("D", "ON value")])
_sr[0] += 2
SWROW = {}
for key, label, default, dvl, on_val, desc in [
    ("prepaid_vs_credit", "Prepaid instead of credit", "Credit", '"Credit,Prepaid"', "Prepaid",
     "ON (Prepaid) caps interchange at 1.00% and removes the credit stream entirely. 'NOT A PRODUCT CHOICE, "
     "IT IS THE BUSINESS MODEL.' Worth ~USD 2.3m of Y10 revenue on the ten-year run."),
    ("lapsed_keeps_card", "Holders keep the card", "ON", '"ON,OFF"', "ON",
     "NOBODY HAS DECIDED THIS. It determines whether the card streams - the majority of revenue - decay with "
     "churn or are immune to it. Worth a 42% swing in terminal revenue. Default ON because nothing in the "
     "design revokes the card; report both."),
]:
    r = _sr[0]
    ws_scen["A%d" % r] = label
    ws_scen["B%d" % r] = '=IF($C$%d="%s",1,0)' % (r, on_val)
    ws_scen["B%d" % r].font = BLACK_BOLD
    ws_scen["B%d" % r].number_format = FMT_NUM
    ws_scen["C%d" % r] = default
    ws_scen["C%d" % r].font = BLUE_BOLD
    ws_scen["D%d" % r] = on_val
    ws_scen["D%d" % r].font = SECONDARY
    ws_scen["G%d" % r] = desc
    ws_scen["G%d" % r].font = NOTE_FONT
    d = DataValidation(type="list", formula1=dvl, allowBlank=False)
    ws_scen.add_data_validation(d)
    d.add(ws_scen["C%d" % r])
    SWROW[key] = r
    SROW["sw_" + key] = r          # so sref() reaches switches too
    SORDER.append("sw_" + key)
    # Label matches the Scenario sheet EXACTLY so the same row is findable on
    # both; the 1/0 nature is carried in the unit column, not the label.
    SMETA["sw_" + key] = (label, "1/0 switch", desc, FMT_NUM)
    declare("sw_" + key, "Scenario Parameters", "$B$%d" % r)
    _sr[0] += 1
ws_scen.freeze_panes = "B8"

# ============================================================================
# ASSUMPTIONS, continued - SCENARIO-LINKED INPUTS
#
# The firm's convention (DRODE): Scenario Parameters holds the Base /
# Aggressive / Conservative columns and picks the live one; ASSUMPTIONS is the
# complete register of every input; and the MODEL reads only from Assumptions.
# So each scenario parameter is mirrored here as a GREEN link to its active
# value. Change the scenario switch and these move with it.
#
# The chain is strictly one-directional:
#     Scenario Parameters  ->  Assumptions  ->  Model  ->  Summary
# ============================================================================
a_section("SCENARIO-LINKED INPUTS (live values - move with the scenario switch)")
SMIRROR = {}
for key in SORDER:
    param, unit, why, fmt = SMETA[key]
    r = _ar[0]
    ws_assum["A%d" % r] = param
    c = ws_assum["B%d" % r]
    c.value = "='Scenario Parameters'!$B$%d" % SROW[key]
    c.font = GREEN
    if fmt:
        c.number_format = fmt
    ws_assum["C%d" % r] = unit
    ws_assum["D%d" % r] = why
    SMIRROR[key] = r
    _ar[0] += 1
note(ws_assum, _ar[0],
     "Every row above is a GREEN link to the active value on Scenario Parameters, which is itself a CHOOSE() "
     "across the Base / Aggressive / Conservative columns. Flip the scenario selector and all of them move. "
     "The Model reads these cells and never reaches into Scenario Parameters directly, so this sheet is the "
     "complete register of every input the model uses.")
_ar[0] += 2


# REBIND: from here on, a scenario reference resolves through the Assumptions
# mirror rather than the Scenario sheet. Everything below (the Model) picks this
# up; the Scenario sheet is already written and keeps its own internal refs.
def sref(k): return "Assumptions!$B$%d" % SMIRROR[k]

# ============================================================================
# MODEL
# ============================================================================
ws_model["A1"] = "=Cover!$B$2"
ws_model["A1"].font = SHEET_TITLE
widths(ws_model, {"A": 52, "B": 18})
for i in range(N_PERIODS):
    ws_model.column_dimensions[pcol(i)].width = 13
MROW, _mr = {}, [2]


def m_row(key, label, unit, fn, fmt=FMT_NUM, font=BLACK, bold=False, total=False):
    r = _mr[0]
    ws_model["A%d" % r] = label
    ws_model["A%d" % r].font = BLACK_BOLD if bold else BLACK
    ws_model["B%d" % r] = unit
    ws_model["B%d" % r].font = SECONDARY
    for i in range(N_PERIODS):
        c = ws_model[pcell(r, i)]
        c.value = fn(i)
        c.font = font
        if fmt:
            c.number_format = fmt
        c.alignment = Alignment(horizontal="center")
        if total:
            c.border = TOTALS_BORDER
    MROW[key] = r
    _mr[0] = r + 1
    return r


def mr(key, i): return pcell(MROW[key], i)
def mrng(key): return "$%s$%d:$%s$%d" % (pcol(0), MROW[key], pcol(N_PERIODS - 1), MROW[key])


# -- period grid -------------------------------------------------------------
m_row("period_idx", "Period #", "1..29", lambda i: i + 1, FMT_NUM, BLACK_BOLD, True)
m_row("period", "Period", "-", lambda i: plabel(i), None, BLACK_BOLD, True)
m_row("period_type", "Period type", "-", lambda i: "Monthly" if is_monthly(i) else "Annual", None)
m_row("year", "Model year", "1..7", lambda i: pyear(i), FMT_NUM)
m_row("cal_month", "Calendar month", "0 = annual", lambda i: cal_month(i), FMT_NUM)
m_row("n", "Months in period", "months", lambda i: n_months(i), FMT_NUM)
m_row("fy_end", "Financial-year end", "1/0", lambda i: 1 if is_fy_end(i) else 0, FMT_NUM)
_mr[0] += 1

# -- activation ---------------------------------------------------------------
# There is no band of 1/0 flag rows. Each stream carries its own activation
# INLINE, reading the month straight from the Assumptions activation calendar,
# so the month still lives in exactly one place and a reader clicking any
# stream cell sees the condition rather than having to find a flag row.
# The only exception is the region gate, which is used twelve times over (three
# regions x four region rows) and so is computed once, below.


def gate(key, i, expr):
    """Wrap a stream calculation in its activation condition."""
    return "=IF(%s>=%s,%s,0)" % (mr("period_idx", i), aref("act_" + key), expr)


def opened(key, i):
    return "IF(%s>=%s,1,0)" % (mr("period_idx", i), aref("act_" + key))

# -- seasonality -------------------------------------------------------------
banner(ws_model, _mr[0], "SEASONALITY - normalised to EXACTLY 12.000 by construction")
_mr[0] += 1
AMP = sref("seasonality_amplitude")


def sq(key, k): return "Assumptions!$%s$%d" % (get_column_letter(SEAS_COL0 + k), SEAS_ROW[key])
def sqr(key): return "Assumptions!$%s$%d:$%s$%d" % (get_column_letter(SEAS_COL0), SEAS_ROW[key],
                                                    get_column_letter(SEAS_COL0 + 11), SEAS_ROW[key])


NORM = {}
for key, label, fmt in (("acq", "Acquisition seasonality - normalised", FMT_NUM3),
                        ("spend", "Card spend seasonality - normalised", FMT_NUM3)):
    r = _mr[0]
    ws_model["A%d" % r] = label
    ws_model["B%d" % r] = "Jan..Dec"
    ws_model["B%d" % r].font = SECONDARY
    for k in range(12):
        c = ws_model.cell(row=r, column=PCOL0 + k)
        c.value = "=(1+(%s-1)*%s)*12/SUMPRODUCT(1+(%s-1)*%s)" % (sq(key, k), AMP, sqr(key), AMP)
        c.font, c.number_format = GREEN, fmt
        c.alignment = Alignment(horizontal="center")
    NORM[key] = r
    _mr[0] += 1
r = _mr[0]
ws_model["A%d" % r] = "Foreign-spend share - rescaled to the mean"
ws_model["B%d" % r] = "Jan..Dec"
ws_model["B%d" % r].font = SECONDARY
for k in range(12):
    c = ws_model.cell(row=r, column=PCOL0 + k)
    c.value = "=%s/AVERAGE(%s)*%s" % (sq("foreign", k), sqr("foreign"), sref("foreign_spend_share"))
    c.font, c.number_format = GREEN, FMT_PCT
    c.alignment = Alignment(horizontal="center")
NORM["foreign"] = r
_mr[0] += 1
r = _mr[0]
ws_model["A%d" % r] = "Seasonality sum check (must be exactly 12.000)"
ws_model["A%d" % r].font = BLACK_BOLD
ws_model["B%d" % r] = "acq | spend"
ws_model["B%d" % r].font = SECONDARY
for k, key in enumerate(("acq", "spend")):
    c = ws_model.cell(row=r, column=PCOL0 + k)
    c.value = "=SUM($%s$%d:$%s$%d)" % (pcol(0), NORM[key], pcol(11), NORM[key])
    c.font, c.number_format = BLACK_BOLD, FMT_NUM3
    declare("seas_sum_" + key, "Model", "$%s$%d" % (pcol(k), r))
MROW["seas_sum"] = r
_mr[0] += 1


def seas(key, i, fmt_annual="1"):
    rng = "$%s$%d:$%s$%d" % (pcol(0), NORM[key], pcol(11), NORM[key])
    if key == "foreign":
        return "IF(%s=1,INDEX(%s,1,%s),AVERAGE(%s))" % (mr("n", i), rng, mr("cal_month", i), rng)
    return "IF(%s=1,INDEX(%s,1,%s),%s)" % (mr("n", i), rng, mr("cal_month", i), fmt_annual)


m_row("seas_acq", "Acquisition seasonality applied", "multiplier",
      lambda i: "=" + seas("acq", i), FMT_NUM3)
m_row("seas_spend", "Card spend seasonality applied", "multiplier",
      lambda i: "=" + seas("spend", i), FMT_NUM3)
m_row("seas_foreign", "Foreign-spend share applied", "%",
      lambda i: "=" + seas("foreign", i), FMT_PCT)
_mr[0] += 1

# ============================ ACQUISITION ===================================
# Total new customers, then split across regions. The referral and saturation
# terms read the WHOLE-BOOK totals at the PREVIOUS period, which live below the
# region blocks - so these rows are reserved here and written once those row
# numbers are known. Referencing a later row at column i-1 is not circular.
banner(ws_model, _mr[0], "ACQUISITION - all channels, then split across regions")
_mr[0] += 1
# Agents are routed to the regions they actually operate in; everything else is
# allocated across open regions by market size. Saturation is applied PER
# REGION, so concentrating a channel in one market cannot push that market past
# its own ceiling while the whole-book total still looks unbreached.
# Only the agent channel is computed centrally, because agent headcount is a
# single national resource routed to the markets it operates in. Marketing and
# referral are now computed INSIDE each region block, because each market has
# its own CAC and its own referring base.
ACQ_ROWS = ["agent_new"]
ACQ_FIRST = _mr[0]
ws_model["A%d" % ACQ_FIRST] = "Agent-driven new customers (routed by region below)"
ws_model["B%d" % ACQ_FIRST] = "accounts"
ws_model["B%d" % ACQ_FIRST].font = SECONDARY
MROW["agent_new"] = ACQ_FIRST
_mr[0] = ACQ_FIRST + len(ACQ_ROWS)
# Renormalisation base: the share of the region mix actually OPEN this period,
# so a region that has not launched redistributes its share rather than losing
# it. Depends only on the mix and the activation calendar, so it is computed
# here - ahead of the region blocks that divide by it.
m_row("open_mix", "Open-region share total (renormalisation base)", "x",
      lambda i: "=" + "+".join(
          "%s*%s" % (sref("mix_" + q), "1" if q not in [a[0] for a in ACTIVATIONS] else opened(q, i))
          for q in REGIONS), FMT_NUM3)
_mr[0] += 1

# ======================== ONE BLOCK PER REGION ==============================
# Each region is self-contained: its own customers, contributions, AUM, cards
# and all six streams, ending in a regional subtotal. The grand total is the
# sum of those subtotals plus the non-regional B2B line.
CHURN = sref("monthly_churn")
NET_FEE = "(%s-(1-%s)*%s)" % (aref("entry_fee"), aref("entry_fee"), aref("fab_premium"))
ATM_TERMS = "+".join(
    "%s*MAX(0,%s-%s)" % (sref("atm_" + k), sref("atmm_" + k), aref("atm_allowance"))
    for k, _n, _b, _a, _c, _mb, _ma, _mc in ATM)
SUBTOTALS = []

for rg in REGIONS:
    banner(ws_model, _mr[0], "REGION: %s" % RLAB[rg].upper())
    _mr[0] += 1
    op = "1" if rg not in [a[0] for a in ACTIVATIONS] else opened(rg, 0)

    def _open(i, rg=rg):
        return "1" if rg not in [a[0] for a in ACTIVATIONS] else opened(rg, i)

    # -- customers ----------------------------------------------------------
    # Raw demand = this region's share of non-agent demand, plus whatever share
    # of agent output actually sells here. Then this region's OWN saturation.
    # direct, referral, raw, sat, new, pay, churn, hold, cum
    _pay_row, _cum_row = _mr[0] + 5, _mr[0] + 8
    m_row("direct_" + rg, "  Direct-driven (this market's budget at its own CAC)", "accounts",
          lambda i, rg=rg: "=INDEX(Assumptions!$B$%d:$B$%d,%s)*%s/12*%s/%s*(1+%s)*%s" % (
              AROW["mktg_y1"], AROW["mktg_y7"], mr("year", i), sref("mktshare_" + rg),
              mr("n", i), sref("cac_" + rg), sref("organic_share"), _open(i, rg)), FMT_NUM2, GREEN)
    m_row("ref_" + rg, "  Referral-driven (from this market's own base)", "accounts",
          lambda i, rg=rg, pr=_pay_row: 0 if i == 0 else gate("referral", i, "%s*%s/12*%s*%s" % (
              pcell(pr, i - 1), sref("referral_rate"), sref("referral_conversion"), mr("n", i))),
          FMT_NUM2)
    m_row("raw_" + rg, "  Raw demand", "accounts",
          lambda i, rg=rg: "=%s+%s+%s*%s" % (
              mr("direct_" + rg, i), mr("ref_" + rg, i),
              mr("agent_new", i), aref("agentshare_" + rg)), FMT_NUM2)
    m_row("sat_" + rg, "  Saturation (this region's own headroom)", "x",
          lambda i, rg=rg, cr=_cum_row: 1 if i == 0 else
          "=MAX(0,1-%s/%s)" % (pcell(cr, i - 1), aref("ceil_" + rg)), FMT_NUM3)
    m_row("new_" + rg, "  New customers", "accounts",
          lambda i, rg=rg: "=%s*%s*%s" % (mr("raw_" + rg, i), mr("sat_" + rg, i),
                                          mr("seas_acq", i)), FMT_NUM2)
    _pr = _mr[0]
    m_row("pay_" + rg, "  Paying customers", "accounts",
          lambda i, rg=rg, pr=_pr: "=%s*(1-%s)^(%s/2)" % (mr("new_" + rg, i), CHURN, mr("n", i)) if i == 0
          else "=%s*(1-%s)^%s+%s*(1-%s)^(%s/2)" % (
              pcell(pr, i - 1), CHURN, mr("n", i), mr("new_" + rg, i), CHURN, mr("n", i)),
          FMT_NUM, BLACK_BOLD)
    assert MROW["pay_" + rg] == _pay_row, \
        "region row layout drifted - the referral lag would read the wrong row"
    m_row("churn_" + rg, "  Churned this period", "accounts",
          lambda i, rg=rg, pr=_pr: "=%s-%s" % (mr("new_" + rg, i), mr("pay_" + rg, i)) if i == 0
          else "=%s+%s-%s" % (pcell(pr, i - 1), mr("new_" + rg, i), mr("pay_" + rg, i)), FMT_NUM2)
    _hr = _mr[0]
    m_row("hold_" + rg, "  Holders (stopped paying, still hold gold)", "accounts",
          lambda i, rg=rg, hr=_hr: "=%s" % mr("churn_" + rg, i) if i == 0
          else "=%s+%s" % (pcell(hr, i - 1), mr("churn_" + rg, i)), FMT_NUM)
    _cr = _mr[0]
    m_row("cum_" + rg, "  Cumulative ever acquired", "accounts",
          lambda i, rg=rg, cr=_cr: "=%s" % mr("new_" + rg, i) if i == 0
          else "=%s+%s" % (pcell(cr, i - 1), mr("new_" + rg, i)), FMT_NUM)
    assert MROW["cum_" + rg] == _cum_row, \
        "region row layout drifted - the saturation lag would read the wrong row"

    # -- contributions and AUM ----------------------------------------------
    m_row("sip_" + rg, "  SIP contributions", "USD",
          lambda i, rg=rg: gate("s1a", i, "%s*%s*%s" % (mr("pay_" + rg, i), sref("ticket_" + rg),
                                                        mr("n", i))), FMT_USD)
    m_row("spot_" + rg, "  Spot purchase volume", "USD",
          lambda i, rg=rg: gate("s1b", i, "%s*%s*%s*%s*%s/12*%s" % (
              mr("pay_" + rg, i), aref("spotmult_" + rg), sref("spot_attach"),
              sref("spot_frequency"), sref("spot_ticket"), mr("n", i))), FMT_USD)
    m_row("grams_in_" + rg, "  Grams purchased", "grams",
          lambda i, rg=rg: "=(%s+%s)*(1-%s)/%s/(1+%s)" % (
              mr("sip_" + rg, i), mr("spot_" + rg, i), aref("entry_fee"),
              aref("gold_price"), aref("fab_premium")), FMT_NUM2)
    m_row("decay_" + rg, "  AUM decay rate (holder-weighted)", "%/period",
          lambda i, rg=rg: "=(%s+%s*IF(%s+%s=0,1,(%s+%s*%s)/(%s+%s)))*%s/12" % (
              sref("self_custody_leakage"), sref("redemption_rate"),
              mr("pay_" + rg, i), mr("hold_" + rg, i),
              mr("pay_" + rg, i), mr("hold_" + rg, i), sref("lapsed_redemption_mult"),
              mr("pay_" + rg, i), mr("hold_" + rg, i), mr("n", i)), FMT_PCT2)
    _gr = _mr[0]
    m_row("grams_" + rg, "  Grams held", "grams",
          lambda i, rg=rg, gr=_gr: "=%s" % mr("grams_in_" + rg, i) if i == 0
          else "=%s*(1-%s)+%s" % (pcell(gr, i - 1), mr("decay_" + rg, i), mr("grams_in_" + rg, i)),
          FMT_NUM)
    m_row("aum_" + rg, "  AUM", "USD",
          lambda i, rg=rg: "=%s*%s" % (mr("grams_" + rg, i), aref("gold_price")), FMT_USD, BLACK_BOLD)

    # -- cards --------------------------------------------------------------
    m_row("cardbase_" + rg, "  Card-eligible base", "accounts",
          lambda i, rg=rg: "=%s+%s*%s" % (mr("pay_" + rg, i), mr("hold_" + rg, i),
                                          sref("sw_lapsed_keeps_card")), FMT_NUM2)
    m_row("qual_" + rg, "  Cleared the six-payment gate", "accounts",
          lambda i, rg=rg: "=IF(%s>1,%s*%s,IF(%s>%s,INDEX(%s,1,%s-%s)*%s,0))" % (
              mr("n", i), mr("cardbase_" + rg, i), sref("ever_qualify"),
              mr("period_idx", i), sref("months_to_qualify"), mrng("cardbase_" + rg),
              mr("period_idx", i), sref("months_to_qualify"), sref("ever_qualify")), FMT_NUM)
    m_row("cards_" + rg, "  Active cards", "cards",
          lambda i, rg=rg: gate("s2", i, "%s*%s" % (mr("qual_" + rg, i), sref("card_activation"))),
          FMT_NUM, BLACK_BOLD)
    # THE CARD IS A DRAWDOWN ON THE GOLD FACILITY (client decision 2026-08-20).
    # Aurumix has no balance sheet to lend from, so credit can only be extended
    # against collateral it holds. Spending on the card IS borrowing, and the
    # customer must repay to release their gold.
    #
    # Card spend is therefore NOT income-based. It is the annual drawdown:
    #     limit (gold x LTV)  x  drawn share  x  draw events per year
    # This is the same facility stream 5 already prices, so both now read one
    # volume instead of two inconsistent ones. Under PREPAID the card is loaded
    # from salary instead, and the gold does not constrain it.
    m_row("limit_" + rg, "  Credit limit per customer (gold x LTV)", "USD",
          lambda i, rg=rg: "=IF(%s=0,0,%s/%s*%s)" % (
              mr("pay_" + rg, i), mr("aum_" + rg, i), mr("pay_" + rg, i), aref("ltv_gold")), FMT_USD)
    m_row("drawyr_" + rg, "  Annual drawdown per card (limit x drawn x draws)", "USD/yr",
          lambda i, rg=rg: "=%s*%s*%s" % (mr("limit_" + rg, i), sref("drawn_share"),
                                          sref("draw_events")), FMT_USD)
    m_row("spendcard_" + rg, "  Card spend per card per month", "USD",
          lambda i, rg=rg: "=%s/12*%s" % (mr("drawyr_" + rg, i), mr("seas_spend", i)), FMT_USD)
    m_row("spendaed_" + rg, "  Card spend", "AED",
          lambda i, rg=rg: "=%s*%s*%s*%s" % (
              mr("cards_" + rg, i), mr("spendcard_" + rg, i), aref("aed_usd"),
              mr("n", i)), FMT_NUM)
    m_row("spendusd_" + rg, "  Card spend", "USD",
          lambda i, rg=rg: "=%s/%s" % (mr("spendaed_" + rg, i), aref("aed_usd")), FMT_USD)
    # Average ticket is DERIVED, never input: monthly spend / transactions. It
    # therefore scales with this region's SIP ticket automatically, and cannot
    # drift to a basket the customer could not fund.
    # The draw events cancel: average ticket = drawn amount / transactions per
    # draw. So it depends only on how big a borrowing is and across how many
    # purchases it is spent - not on how often the customer borrows.
    m_row("avgtxn_" + rg, "  Average transaction size (derived)", "AED",
          lambda i, rg=rg: "=IF(%s=0,0,%s*%s*%s/%s)" % (
              sref("card_txns_per_draw"), mr("limit_" + rg, i), sref("drawn_share"),
              aref("aed_usd"), sref("card_txns_per_draw")), FMT_NUM)
    # MEMO for the cost build - the processor bills per AUTHORISATION, which is
    # draws x transactions per draw, grossed up for declines. Feeds no revenue.
    m_row("auths_" + rg, "  Card authorisations (memo - drives cost, not revenue)", "auths",
          lambda i, rg=rg: "=%s*%s*%s*%s/12*(1+%s)" % (
              mr("cards_" + rg, i), sref("draw_events"), sref("card_txns_per_draw"),
              mr("n", i), aref("decline_uplift")), FMT_NUM)

    # -- the six streams, plus the redemption cost --------------------------
    m_row("s1a_" + rg, "  Stream 1a - Entry fee margin, SIP", "USD",
          lambda i, rg=rg: "=%s*%s" % (mr("sip_" + rg, i), NET_FEE), FMT_USD)
    m_row("s1b_" + rg, "  Stream 1b - Entry fee margin, SPOT", "USD",
          lambda i, rg=rg: "=%s*%s" % (mr("spot_" + rg, i), NET_FEE), FMT_USD)
    m_row("s2_" + rg, "  Stream 2 - Card interchange", "USD",
          lambda i, rg=rg: "=%s*IF(%s=1,MIN(%s,1%%),%s)*(1-%s)" % (
              mr("spendusd_" + rg, i), sref("sw_prepaid_vs_credit"), aref("ic_gold"),
              aref("ic_gold"), sref("pm_share")), FMT_USD)
    m_row("s3_" + rg, "  Stream 3 - Family plan and Digital Will", "USD",
          lambda i, rg=rg: gate("s3", i, "%s*%s*%s/12*%s" % (
              mr("pay_" + rg, i), sref("family_attach"), aref("family_price"), mr("n", i))), FMT_USD)
    m_row("s4_" + rg, "  Stream 4 - Cardholder fees (FX, ATM, events)", "USD",
          lambda i, rg=rg: gate("s4", i, "%s*%s*%s+%s*(%s)*%s/%s*%s+%s*(%s*%s+%s*%s)/12/%s*%s" % (
              mr("spendusd_" + rg, i), mr("seas_foreign", i), aref("fx_margin"),
              mr("cards_" + rg, i), ATM_TERMS, aref("atm_fee"), aref("aed_usd"), mr("n", i),
              mr("cards_" + rg, i), sref("issuance_events"), aref("issuance_fee"),
              sref("replacement_events"), aref("replacement_fee"), aref("aed_usd"), mr("n", i))),
          FMT_USD)
    # Stream 5 reads THE SAME facility and the same cardholder population as
    # streams 2 and 4. Interchange comes from the merchant, lending fees from
    # the borrower - two payers on one drawdown, which is not double-counting,
    # but the VOLUME must be a single number, and now is.
    m_row("drawn_" + rg, "  Average drawn balance outstanding", "USD",
          lambda i, rg=rg: gate("s5", i, "%s*%s*(1-%s)*%s*%s" % (
              mr("cards_" + rg, i), mr("limit_" + rg, i), sref("sw_prepaid_vs_credit"),
              sref("drawn_share"), sref("facility_turnover"))), FMT_USD)
    m_row("s5_" + rg, "  Stream 5 - Lending revenue share", "USD",
          lambda i, rg=rg: gate("s5", i, "(%s*%s*%s+%s*%s*(1-%s)*%s*%s)*%s/12" % (
              mr("drawn_" + rg, i), aref("servicing_gross"), aref("servicing_share"),
              mr("cards_" + rg, i), mr("drawyr_" + rg, i), sref("sw_prepaid_vs_credit"),
              aref("origination_gross"), aref("origination_share"), mr("n", i)), ), FMT_USD)
    # MEMO for the cost build - redemption is a COST with no offsetting revenue
    # (VARA forbids charging for it), so the event count is carried here and the
    # cost itself arrives with the cost build. It feeds no total.
    m_row("redem_" + rg, "  Redemption events (memo - drives cost, not revenue)", "events",
          lambda i, rg=rg: gate("s0", i, "(%s+%s*%s)*%s*%s/12" % (
              mr("pay_" + rg, i), mr("hold_" + rg, i), sref("lapsed_redemption_mult"),
              sref("redemption_rate"), mr("n", i))), FMT_NUM)
    m_row("sub_" + rg, "  SUBTOTAL - %s" % RLAB[rg], "USD",
          lambda i, rg=rg: "=" + "+".join(mr("%s_%s" % (s, rg), i)
                                          for s in ("s1a", "s1b", "s2", "s3", "s4", "s5")),
          FMT_USD, BLACK_BOLD, True)
    SUBTOTALS.append("sub_" + rg)
    _mr[0] += 1

# ===================== NON-REGIONAL AND GRAND TOTAL =========================
banner(ws_model, _mr[0], "NON-REGIONAL")
_mr[0] += 1
m_row("partner_aum", "  Partner AUM", "USD",
      lambda i: gate("s6", i, "INDEX(Assumptions!$B$%d:$B$%d,%s)*%s" % (
          SMIRROR["partners_y1"], SMIRROR["partners_y7"], mr("year", i),
          sref("aum_per_partner"))), FMT_USD, GREEN)
# NOT indented: this is a whole-book stream in its own right, not a sub-item of
# a region block, and the indentation is what distinguishes the two.
m_row("s6", "Stream 6 - B2B platform fee", "USD",
      lambda i: "=%s*%s*%s/12" % (mr("partner_aum", i), aref("b2b_fee"), mr("n", i)),
      FMT_USD, BLACK_BOLD)
note(ws_model, _mr[0],
     "Stream 6 is NOT regional: partners are institutions with their own customer books, not retail "
     "customers of a region. It is reported separately rather than allocated, because any allocation would "
     "be invented.")
_mr[0] += 2

banner(ws_model, _mr[0], "WHOLE-BOOK TOTALS")
_mr[0] += 1
for key, label, parts, fmt, bold in (
    ("paying", "PAYING CUSTOMERS", ["pay_" + r for r in REGIONS], FMT_NUM, True),
    ("holders", "HOLDERS (stopped paying, still hold gold)", ["hold_" + r for r in REGIONS], FMT_NUM, True),
    ("cum_ever", "Cumulative ever acquired", ["cum_" + r for r in REGIONS], FMT_NUM, False),
    ("new_total", "NEW CUSTOMERS", ["new_" + r for r in REGIONS], FMT_NUM, True),
    ("active_cards", "ACTIVE CARDS", ["cards_" + r for r in REGIONS], FMT_NUM, True),
    ("grams_held", "GRAMS HELD", ["grams_" + r for r in REGIONS], FMT_NUM, False),
    ("aum", "AUM", ["aum_" + r for r in REGIONS], FMT_USD, True),
    ("qualified", "Cleared the six-payment gate", ["qual_" + r for r in REGIONS], FMT_NUM, False),
    ("sip_inflow", "SIP contributions", ["sip_" + r for r in REGIONS], FMT_USD, False),
    ("spot_inflow", "Spot purchase volume", ["spot_" + r for r in REGIONS], FMT_USD, False),
    ("card_spend_usd", "Card spend", ["spendusd_" + r for r in REGIONS], FMT_USD, False),
):
    m_row(key, label, "-", lambda i, p=parts: "=" + "+".join(mr(x, i) for x in p), fmt, BLACK, bold)
m_row("conservation", "CHECK: paying + holders = cumulative ever acquired", "delta",
      lambda i: "=%s+%s-%s" % (mr("paying", i), mr("holders", i), mr("cum_ever", i)), FMT_NUM3, BLACK_BOLD)
# Sanity memo: under the credit variant the card is secured on the customer's
# own gold, so the limit that gold supports is a hard ceiling on monthly spend.
m_row("aum_per_cust", "  AUM per paying customer (memo)", "USD",
      lambda i: "=IF(%s=0,0,%s/%s)" % (mr("paying", i), mr("aum", i), mr("paying", i)), FMT_USD)
# Total monthly card spend against TOTAL credit capacity - capacity summed as
# cards x that region's own limit. Dividing blended spend by a PAYING-weighted
# limit is the wrong aggregation: cards concentrate in the older, higher-limit
# regions, so that version reads above 1.00 even when every region is inside
# its own cap. NB the summed spend must be bracketed before dividing.
m_row("credit_capacity", "  Total credit capacity across cardholders (memo)", "USD",
      lambda i: "=" + "+".join("%s*%s" % (mr("cards_" + r, i), mr("limit_" + r, i)) for r in REGIONS),
      FMT_USD)
m_row("spend_vs_limit", "  CHECK: card spend vs credit capacity (must be <= 1.00)", "x",
      lambda i: "=IF(%s=0,0,((%s)/%s)/%s)" % (
          mr("credit_capacity", i), "+".join(mr("spendusd_" + r, i) for r in REGIONS),
          mr("n", i), mr("credit_capacity", i)), '0.00"x"', BLACK_BOLD)
_mr[0] += 1

for key, label, parts in (
    ("s1a", "Stream 1a - Entry fee margin, SIP", ["s1a_" + r for r in REGIONS]),
    ("s1b", "Stream 1b - Entry fee margin, SPOT", ["s1b_" + r for r in REGIONS]),
    ("s2", "Stream 2 - Card interchange", ["s2_" + r for r in REGIONS]),
    ("s3", "Stream 3 - Family plan and Digital Will", ["s3_" + r for r in REGIONS]),
    ("s4", "Stream 4 - Cardholder fees", ["s4_" + r for r in REGIONS]),
    ("s5", "Stream 5 - Lending revenue share", ["s5_" + r for r in REGIONS]),
    ("redemptions", "Redemption events (memo - drives cost, not revenue)",
     ["redem_" + r for r in REGIONS]),
    ("auths", "Card authorisations (memo - drives cost, not revenue)",
     ["auths_" + r for r in REGIONS]),
):
    _memo = key in ("redemptions", "auths")
    m_row(key, label, "events" if _memo else "USD",
          lambda i, p=parts: "=" + "+".join(mr(x, i) for x in p),
          FMT_NUM if _memo else FMT_USD)
m_row("total_rev", "TOTAL NET REVENUE", "USD",
      lambda i: "=" + "+".join(mr(s, i) for s in SUBTOTALS) + "+" + mr("s6", i),
      FMT_USD, BLACK_BOLD, True)
m_row("rev_per_cust", "Net revenue per paying customer (annualised)", "USD",
      lambda i: "=IF(%s=0,0,%s/%s/%s*12)" % (mr("paying", i), mr("total_rev", i),
                                             mr("paying", i), mr("n", i)), FMT_USD)
m_row("total_check", "CHECK: regional subtotals + B2B = sum of streams", "delta",
      lambda i: "=%s-(%s)" % (mr("total_rev", i),
                              "+".join(mr(s, i) for s in
                                       ("s1a", "s1b", "s2", "s3", "s4", "s5", "s6"))),
      FMT_NUM3, BLACK_BOLD)

# ---- now fill the reserved acquisition rows -------------------------------
CEIL = "+".join(aref("ceil_" + k) for k in REGIONS)
for key, fn, fmt, font in (
    ("agent_new", lambda i: "=INDEX(Assumptions!$B$%d:$B$%d,%s)*%s*INDEX(Assumptions!$B$%d:$B$%d,%s)*%s"
     % (AROW["agents_y1"], AROW["agents_y7"], mr("year", i), sref("agent_productivity"),
        AROW["ramp_y1"], AROW["ramp_y7"], mr("year", i), mr("n", i)), FMT_NUM2, GREEN),
):
    for i in range(N_PERIODS):
        c = ws_model[pcell(MROW[key], i)]
        c.value = fn(i)
        c.font = font
        c.number_format = fmt
        c.alignment = Alignment(horizontal="center")

ws_model.freeze_panes = "C8"


# ============================================================================
# SUMMARY
# ============================================================================
ws_summ["A1"] = "=Cover!$B$2"
ws_summ["A1"].font = SHEET_TITLE
ws_summ["A2"] = "Summary"
ws_summ["A2"].font = SHEET_SUB
widths(ws_summ, {"A": 46, "B": 4, **{ycol(y): 16 for y in range(1, N_YEARS + 1)}})
for y in range(1, N_YEARS + 1):
    c = ws_summ["%s4" % ycol(y)]
    c.value, c.fill, c.font, c.border = "Y%d" % y, HEADER_FILL, HEADER_FONT, BORDER
    c.alignment = Alignment(horizontal="center")


def yr_expr(key, y, how="sum"):
    """Y1/Y2 aggregate the twelve monthly columns; Y3-Y7 are single columns."""
    if y <= 2:
        lo, hi = (y - 1) * 12, y * 12 - 1
        if how == "sum":
            return "=SUM(Model!%s:%s)" % (mr(key, lo), mr(key, hi))
        return "=Model!%s" % mr(key, hi)
    return "=Model!%s" % mr(key, N_MONTHLY + y - 3)


_sy = [6]


def s_block(title, rows):
    """Emit a Summary block and RETURN {key: row}, so anything that needs to
    reference these rows reads the real row number instead of a hardcoded one.
    Hardcoding is what broke the revenue mix when a block was inserted above it."""
    r = _sy[0]
    section(ws_summ, r, title, span=11)
    _sy[0] = r + 1
    placed = {}
    for key, label, how, fmt, bold in rows:
        rr = _sy[0]
        ws_summ["A%d" % rr] = label
        ws_summ["A%d" % rr].font = BLACK_BOLD if bold else BLACK
        for y in range(1, N_YEARS + 1):
            c = ws_summ["%s%d" % (ycol(y), rr)]
            c.value = yr_expr(key, y, how)
            c.font, c.number_format = GREEN, fmt
            if bold:
                c.border = TOTALS_BORDER
        placed[key] = rr
        _sy[0] += 1
    _sy[0] += 1
    return placed


REG_ROWS = s_block("REVENUE BY REGION", [
    (s, "  %s" % RLAB[s[4:]], "sum", FMT_USD, False) for s in SUBTOTALS
] + [
    ("s6", "  Non-regional: B2B platform fee", "sum", FMT_USD, False),
    ("total_rev", "TOTAL REVENUE", "sum", FMT_USD, True),
])

STREAM_ROWS = s_block("REVENUE BY STREAM", [
    ("s1a", "Stream 1a: Entry fee margin - SIP", "sum", FMT_USD, False),
    ("s1b", "Stream 1b: Entry fee margin - SPOT", "sum", FMT_USD, False),
    ("s2", "Stream 2: Card interchange", "sum", FMT_USD, False),
    ("s3", "Stream 3: Family plan and Digital Will", "sum", FMT_USD, False),
    ("s4", "Stream 4: Cardholder fees", "sum", FMT_USD, False),
    ("s5", "Stream 5: Lending revenue share", "sum", FMT_USD, False),
    ("s6", "Stream 6: B2B platform fee", "sum", FMT_USD, False),
    # Same number as the regional total above - shown again as a reconciliation,
    # labelled distinctly so the two are never read as separate figures.
    ("total_rev", "Total by stream (reconciles to the regional total above)", "sum", FMT_USD, True),
])

# Mix rows reference the ACTUAL row numbers returned above. These were once
# hardcoded, and inserting a block above them silently pointed every percentage
# at the wrong numerator and the wrong denominator.
TOT_ROW = REG_ROWS["total_rev"]
r = _sy[0]
section(ws_summ, r, "REVENUE MIX (% of total)", span=11)
_sy[0] = r + 1
# Labels are suffixed so they are DISTINCT from the dollar rows above. Two rows
# on one sheet sharing a label is how a lookup silently reads dollars as a
# percentage - which is exactly what happened when this block was first read.
for key, label in [("s1a", "Stream 1a: SIP entry fee - share"),
                   ("s1b", "Stream 1b: Spot entry fee - share"),
                   ("s2", "Stream 2: Card interchange - share"),
                   ("s3", "Stream 3: Family and Will - share"),
                   ("s4", "Stream 4: Cardholder fees - share"),
                   ("s5", "Stream 5: Lending - share"),
                   ("s6", "Stream 6: B2B platform - share")]:
    rr = _sy[0]
    ws_summ["A%d" % rr] = label
    for y in range(1, N_YEARS + 1):
        c = ws_summ["%s%d" % (ycol(y), rr)]
        c.value = "=IF(%s$%d=0,0,%s%d/%s$%d)" % (ycol(y), TOT_ROW, ycol(y),
                                                 STREAM_ROWS[key], ycol(y), TOT_ROW)
        c.font, c.number_format = BLACK, FMT_PCT
    _sy[0] += 1
rr = _sy[0]
ws_summ["A%d" % rr] = "CHECK: mix sums to 100%"
ws_summ["A%d" % rr].font = BLACK_BOLD
for y in range(1, N_YEARS + 1):
    c = ws_summ["%s%d" % (ycol(y), rr)]
    c.value = "=SUM(%s%d:%s%d)" % (ycol(y), _sy[0] - 7, ycol(y), _sy[0] - 1)
    c.font, c.number_format = BLACK_BOLD, FMT_PCT
MIX_CHECK_ROW = rr
_sy[0] += 2

s_block("CUSTOMERS AND AUM (year end)", [
    ("new_total", "New customers in year", "sum", FMT_NUM, False),
    ("paying", "Paying customers", "close", FMT_NUM, True),
    ("holders", "Holders (stopped paying, still hold gold)", "close", FMT_NUM, False),
    ("cum_ever", "Cumulative ever acquired", "close", FMT_NUM, False),
    ("active_cards", "Active cards", "close", FMT_NUM, False),
    ("grams_held", "Grams held", "close", FMT_NUM, False),
    ("aum", "AUM", "close", FMT_USD, True),
    ("rev_per_cust", "Net revenue per paying customer (annualised)", "close", FMT_USD, False),
])
note(ws_summ, _sy[0],
     "REVENUE ONLY. Operating costs, tax, working capital, cash and funding are added in a later build, so "
     "there is no profit or break-even line here. Stream 1 IS reported net of the fabrication premium, "
     "because that is cost OF REVENUE rather than an operating cost - reporting it gross would read ~43% high.")

# ============================================================================
registered, rejected = 0, []
for nm, ref in sorted(NAMED):
    try:
        wb.defined_names.add(DefinedName(nm, attr_text=ref))
        registered += 1
    except Exception as exc:                              # noqa: BLE001
        rejected.append((nm, ref, str(exc)))
wb.save(OUTPUT)

print("=" * 78)
print("AURUMIX REVENUE MODEL  -  simplified single build")
print("=" * 78)
print("Output       : %s" % OUTPUT)
print("Sheets       : %s" % " | ".join(wb.sheetnames))
print("Periods      : %d (%d monthly + %d annual), columns %s..%s, M1 = Jan %d"
      % (N_PERIODS, N_MONTHLY, N_ANNUAL, pcol(0), pcol(N_PERIODS - 1), START_YEAR))
print("Rows         : Assumptions %d | Scenario %d | Model %d | Summary %d"
      % (_ar[0], _sr[0], _mr[0], _sy[0]))
print("Scenario     : %d parameters + 2 structural switches" % len(SROW))
print("Named ranges : %d registered, %d rejected" % (registered, len(rejected)))
for nm, ref, exc in rejected:
    print("   REJECTED %-28s %-36s %s" % (nm, ref, exc))
print("-" * 78)
print("Engine       : rolling balance, opening + new - churned = closing, by region")
print("Kept as inputs, not engines:")
print("  - card eligibility (%% who ever qualify, months to qualify)")
print("  - the HOLDERS balance (stopped paying, still hold gold)")
print("  - the fabrication premium netted inside stream 1")
print("  - the ATM draw distribution (a mean returns exactly zero)")
print("Deleted to the Phase 5 simulation: archetypes, run-of-6 chain, lifecycle")
print("  curves, the convolution, the six-state machine, withdrawal buckets.")
print("Out of scope for now: opex, tax, working capital, cash, funding.")
print("=" * 78)
