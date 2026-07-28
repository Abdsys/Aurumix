#!/usr/bin/env python3
"""
Stitch the section files and protocol profiles into one markdown deliverable,
and split the per-protocol SOURCES blocks out into Appendix B.

Section 4 is tiered: five protocols carry full profiles, the remaining eleven
are held in comparison tables that preserve the same nine fields as columns.
Section 5 tiers the same way, with one full profile and two in a table.

Source URLs are read from the uncompressed originals in _original/, which stay
on disk as the provenance record. The compressed body files carry no SOURCES
blocks.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.dirname(HERE)
ORIG = os.path.join(W, "_original")

OUT_MD = os.path.join(W, "Aurumix_Market_Research_Summary.md")
OUT_APPB = os.path.join(W, "appendix-b.md")

# Compressed body files, in document order.
BODY_LIVE = ["prof-live-detailed-1.md", "prof-live-detailed-2.md", "prof-live-table.md"]
BODY_FAILED = "prof-failed.md"

# Uncompressed originals, read only for their SOURCES blocks.
SOURCE_FILES = ["profiles-a.md", "profiles-b.md", "profiles-c.md", "profiles-d.md", "profiles-e.md"]

# Appendix B is a reading aid, not the evidence register. The full register
# lives in Aurumix_Protocol_Landscape.md; listing all 202 URLs here cost six
# pages of the summary.
MAX_SOURCES_PER_PROTOCOL = 6


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read().replace("\r\n", "\n")


def extract_sources(text):
    """Return [(protocol_name, [urls])] from the '## SOURCES:' blocks."""
    parts = re.split(r"^##\s+SOURCES:\s*(.+?)\s*$", text, flags=re.M)
    blocks = []
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        urls = []
        for line in parts[i + 1].split("\n"):
            m = re.match(r"^[-*]\s+(.*)$", line.strip())
            if m:
                u = re.sub(r"^<|>$", "", m.group(1).strip())
                if u:
                    urls.append(u)
        blocks.append((name, urls))
    return blocks


def clean(text):
    text = text.replace("—", ": ")          # any surviving em dash
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    s13 = clean(read(os.path.join(W, "sections-1-3.md")))
    s612 = clean(read(os.path.join(W, "sections-6-12.md")))
    live = "\n\n".join(clean(read(os.path.join(W, n))) for n in BODY_LIVE)
    failed = clean(read(os.path.join(W, BODY_FAILED)))

    doc = []
    doc.append("# Tokenized Gold: Market Research Summary")
    doc.append("")
    doc.append(s13)
    doc.append("")
    doc.append("## 4. Live Protocol Profiles")
    doc.append("")
    doc.append(
        "Sixteen protocols are live. Five carry a full profile, each because it "
        "settles a question this design has to answer:"
    )
    doc.append("")
    doc.append("- **Tether Gold.** What the largest product in the category charges.")
    doc.append("- **Pax Gold.** What a fully licensed issuer looks like.")
    doc.append("- **Kinesis.** Whether an advertised yield survives its own arithmetic.")
    doc.append("- **Streamex.** Whether gold-leasing income can be documented.")
    doc.append("- **Comtech Gold.** What a Dubai issuer actually holds.")
    doc.append("")
    doc.append(
        "The remaining eleven follow in comparison tables carrying the same nine "
        "fields. Where a field records that something is not disclosed, that is "
        "the finding rather than a gap in the research."
    )
    doc.append("")
    doc.append(live)
    doc.append("")
    doc.append("## 5. Protocols That Failed")
    doc.append("")
    doc.append(
        "Three protocols stopped operating, and all three carry more transferable "
        "lessons than most of the live products, because each failed for a reason "
        "that applies directly to a monthly savings model. The Perth Mint Gold "
        "Token is profiled in full. Digix and CACHE Gold follow in a table."
    )
    doc.append("")
    doc.append(failed)
    doc.append("")
    doc.append(s612)
    doc.append("")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(doc).rstrip() + "\n")

    # ---- Appendix B ----
    all_sources = []
    for name in SOURCE_FILES:
        all_sources.extend(extract_sources(read(os.path.join(ORIG, name))))

    lines = [
        "# Appendix B",
        "",
        "The principal sources behind the claims in this report, grouped by "
        "protocol: company and regulator registers, issuer terms and conditions, "
        "filings, attestation and audit reports, and block explorers. Aggregator "
        "listings were used to enumerate the market and are not cited as evidence "
        "about any issuer. The complete source register sits in the accompanying "
        "protocol landscape document.",
        "",
    ]
    seen = set()
    kept = 0
    for name, urls in all_sources:
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        lines.append("#### %s" % name)
        lines.append("")
        for u in urls[:MAX_SOURCES_PER_PROTOCOL]:
            lines.append("- %s" % u)
            kept += 1
        lines.append("")

    with open(OUT_APPB, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")

    body = open(OUT_MD, encoding="utf-8").read()
    print("markdown:   %s" % OUT_MD)
    print("            %d lines, %d words" % (len(body.split("\n")), len(body.split())))
    print("appendix b: %d protocols, %d urls" % (len(seen), kept))


if __name__ == "__main__":
    main()
