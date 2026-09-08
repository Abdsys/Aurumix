#!/usr/bin/env python3
"""Assemble final/Aurumix_Process_Maps.md from the sixteen Phase 2 map sets.

Pulls the selected diagrams (heading + first mermaid block after it), renumbers
them against the mechanism design document's sections, and writes one file for
the branded build to embed. Speaker notes are deliberately dropped: they are
call material, not document material.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHASE = os.path.dirname(HERE)
OUT = os.path.join(PHASE, "final", "Aurumix_Process_Maps.md")

# (source file, heading regex, new id, new title, description)
SELECT = [
    # Section 2: the underlying asset
    ("Aurumix_Process_Maps.md", r"^## 6\. Token Denomination", "2a", "Token denomination: 1 AURX = 1 gram",
     "Why the token count is the gram count, and what that fixes."),
    ("Aurumix_Process_Maps.md", r"^## 3\. The Premium: Three Ways It Fails", "2b", "The premium: three ways it fails",
     "Liquid markets arbitrage it away, illiquid markets cannot express it, and it is not Aurumix's to promise."),
    # Section 3: legal structure
    ("Aurumix_Process_Maps_Ownership_Structure.md", r"^## 1\. The Two Doors", "3a", "The classification fork",
     "Direct-ownership ARVA against stable-value ARVA: what each costs."),
    ("Aurumix_Process_Maps_Ownership_Structure.md", r"^## 3\. Three Ways to Put the Gold Beyond Reach", "3b", "Three ways to put the gold beyond reach",
     "Caretaker contract, DIFC vehicle, or naming customers at the vault."),
    ("Aurumix_Process_Maps_Ownership_Structure.md", r"^## 4\. The Entity Map", "3c", "The entity map",
     "Issuer, technology company, holding vehicle and the contracted partners."),
    ("Aurumix_Process_Maps_Composability.md", r"^## 4\. What Moves When the Token Moves", "3d", "What moves when the token moves",
     "Under the class-defined trust, the transfer is the change of ownership."),
    # Section 4: token architecture
    ("Aurumix_Process_Maps_Composability.md", r"^## 5\. Identity at the Two Doors", "4a", "Identity at the two doors",
     "KYC at mint and redemption; freedom in the room."),
    ("Aurumix_Process_Maps_Composability.md", r"^## 7\. One Hook, Two Settings", "4b", "One hook, two settings",
     "The blocklist ships; the allowlist is the engineered fallback."),
    ("Aurumix_Process_Maps_Composability.md", r"^## 6\. Why the Wrapper Fails", "4c", "Why the wrapper fails",
     "A permissioned base with an open wrapper gives the wrapped holder no gold."),
    # Section 5: buying
    ("Aurumix_Process_Maps_Minting.md", r"^## 1\. One Pipe, Two Doors", "5a", "One pipe, two doors",
     "SIP and spot run the identical purchase pipeline."),
    ("Aurumix_Process_Maps_Minting.md", r"^## 3\. Money, Then Title, Then Token", "5b", "Money, then title, then token",
     "The ordering rule on every purchase, and why the mint halts if title cannot be recorded."),
    ("Aurumix_Process_Maps_Minting.md", r"^## 4\. Worked Example", "5c", "What USD 75 buys",
     "One contribution walked end to end."),
    ("Aurumix_Process_Maps_SIP_Structure.md", r"^## 5\. A Month That Goes Wrong", "5d", "A month that goes wrong",
     "The 5-day grace window, the hard floor, and what a miss does and does not cost."),
    # Section 6: float
    ("Aurumix_Process_Maps.md", r"^## 9\. The Lumpiness Problem", "6a", "The lumpiness problem",
     "Retail tickets against wholesale bars."),
    ("Aurumix_Process_Maps.md", r"^## 11\. The Float: How It Works", "6b", "The float: how it works",
     "Grams move from the float to the customer the same day; the treasury replenishes on a threshold."),
    ("Aurumix_Process_Maps.md", r"^## 13\. The Float Fixes the Buyback", "6c", "The float fixes the buyback",
     "Exits return grams to the float; the next buyer consumes them."),
    # Section 7: exit
    ("Aurumix_Process_Maps_Redemption.md", r"^## 1\. The Exit Path", "7a", "The exit path",
     "Checks, next fix, burn, title return, payout."),
    ("Aurumix_Process_Maps_Redemption.md", r"^## 5\. Why a Zero-Fee Exit Is Affordable", "7b", "Why a zero-fee exit is affordable",
     "The dealer spread is paid on net outflow, not gross exits."),
    ("Aurumix_Process_Maps_Redemption.md", r"^## 6\. When the Float Is Not Enough", "7c", "When the float is not enough",
     "The disclosed, size-tiered settlement windows."),
    # Section 8: ICS
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 0\. The Gate", "8a", "The gate",
     "Six consecutive contributions open the score. Permanent once earned."),
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 2\. The Formula", "8b", "The formula",
     "min(Record, Standing) x Retention."),
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 5a\. The Ladder: Names and Scores", "8c", "The ladder",
     "Five tiers, four named, at 25 / 50 / 75 / 100."),
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 6\. The Climb", "8d", "The climb",
     "Silver at six months, Gold at one year, Platinum at three, Sovereign at five."),
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 7\. The Miss", "8e", "The miss",
     "A miss reduces Recent for twelve months, then ages out. Nothing else happens."),
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 8\. The Cycler", "8f", "The cycler",
     "A flawless payment record with no held gold floors at Silver forever."),
    # Section 9: benefits
    ("Aurumix_Process_Maps_ICS_Scoring.md", r"^## 5b\. What Unlocks at Each Tier", "9a", "What unlocks at each tier",
     "The full tier by benefit matrix."),
    ("Aurumix_Process_Maps_ICS_Benefits.md", r"^## 1b\. The Discount, Worked", "9b", "The entry-fee discount, worked",
     "What the ladder is worth to a USD 75 saver, in grams."),
    # Section 10: credit and card
    ("Aurumix_Process_Maps_Credit_And_Card.md", r"^## 0\. One Facility, Two Draws", "10a", "One facility, two draws",
     "The cash channel and the card channel spend the same limit."),
    ("Aurumix_Process_Maps_Credit_And_Card.md", r"^## 6\. A Card Tap in Three Seconds", "10b", "A card tap in three seconds",
     "Just-in-time authorisation against live collateral headroom."),
    ("Aurumix_Process_Maps_Credit_And_Card.md", r"^## 9\. The Liquidation Ladder", "10c", "The liquidation ladder",
     "Notice at 85, cure at 88, partial sale at 92 restoring 88."),
    ("Aurumix_Process_Maps_Credit_And_Card.md", r"^## 10\. Who Is Actually Exposed", "10d", "Who is actually exposed",
     "The gold fall each tier needs before the ladder bites."),
    # Section 11: family
    ("Aurumix_Process_Maps_Family_And_Succession.md", r"^## 0\. How It Works, End to End", "11a", "The family product, end to end",
     "Registration, triggers, authority, execution."),
    ("Aurumix_Process_Maps_Family_And_Succession.md", r"^## 3\. Three Triggers, Three Different Events", "11b", "Three triggers, three different legal events",
     "Date and condition are lifetime gifts; death is succession."),
    ("Aurumix_Process_Maps_Family_And_Succession.md", r"^## 4\. Where Your Family Lives Changes the Answer", "11c", "Where your family lives changes the answer",
     "The residence matrix, and why India inverts it."),
    ("Aurumix_Process_Maps_Family_And_Succession.md", r"^## 5\. What Happens When Someone Dies", "11d", "What happens when someone dies",
     "Freeze, grant of probate, verification, then one token movement."),
    ("Aurumix_Process_Maps_Family_And_Succession.md", r"^## 6\. If You Borrowed Against Your Gold", "11e", "If you borrowed against your gold",
     "The lender outranks the beneficiary; the beneficiary may redeem by paying."),
    # Section 12: distribution
    ("Aurumix_Process_Maps_Referrals.md", r"^## 0\. How a Referral Works", "12a", "How a referral works",
     "The referee passes their own gate; both sides are paid in grams."),
    ("Aurumix_Process_Maps_Referrals.md", r"^## 3\. One Level, and It Stops There", "12b", "One level, and it stops there",
     "The wall between a bounty and an annuity."),
    # Section 13: fees and revenue
    ("Aurumix_Process_Maps_Payments.md", r"^## 4\. The Four Payment Paths", "13a", "The four payment paths",
     "Every customer ends in the same client account; Aurumix only ever receives bank money."),
    ("Aurumix_Process_Maps_Revenue_Streams.md", r"^## 6b\. The B2B Platform Fee", "13b", "The B2B platform fee",
     "Partners pay monthly on the assets their customers hold."),
    # Section 15: risk
    ("Aurumix_Process_Maps_Composability.md", r"^## 8\. The Four Links Composability Rests On", "15a", "The four links composability rests on",
     "The assumptions register drawn: what breaks if each link fails."),
]

def extract(path, head_re):
    text = io.open(path, encoding="utf-8").read()
    lines = text.splitlines()
    start = None
    for i, l in enumerate(lines):
        if re.match(head_re, l):
            start = i
            break
    if start is None:
        return None
    # find end of this section (next ## or #) after start
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^#{1,2} ", lines[j]):
            end = j
            break
    section = lines[start:end]
    # find mermaid block
    m0 = None
    for k, l in enumerate(section):
        if l.strip().startswith("```mermaid"):
            m0 = k
            break
    if m0 is None:
        return None
    m1 = None
    for k in range(m0 + 1, len(section)):
        if section[k].strip() == "```":
            m1 = k
            break
    if m1 is None:
        return None
    return "\n".join(section[m0:m1 + 1])

def main():
    parts = [
        "# Aurumix Process Maps",
        "",
        "> The diagram set for the Aurumix Mechanism Design Document. Each diagram is",
        "> numbered by the document section it belongs to. Extracted from the Phase 2",
        "> map sets and verified against the decision log; the full sets with speaker",
        "> notes remain in `deliverables/2-mechanism-design/`.",
        "",
    ]
    missing = []
    for fname, head_re, did, title, desc in SELECT:
        path = os.path.join(PHASE, fname)
        block = extract(path, head_re)
        if block is None:
            missing.append((fname, head_re))
            continue
        parts += [f"## {did}. {title}", "", desc, "", block, "", "---", ""]
    io.open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(parts))
    print("written:", OUT)
    print("diagrams:", len(SELECT) - len(missing))
    for m in missing:
        print("MISSING:", m)

if __name__ == "__main__":
    main()
