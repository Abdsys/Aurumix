#!/usr/bin/env python3
"""Style and leakage lint for the client-facing deliverable."""
import os
import re
import sys

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The assembled deliverable plus its two appendices. Linting the assembled file
# rather than the body fragments also covers the section intros written by
# assemble.py. The uncompressed originals in _original/ are provenance, not
# deliverable content, and are deliberately not linted.
FILES = ["Aurumix_Market_Research_Summary.md", "appendix-a.md", "appendix-b.md"]

CHECKS = [
    ("em dash", r"—"),
    ("emoji / glyph", r"[✅❌⚠\U0001F534\U0001F7E1⭐\U0001F527▶⏭\U0001F4C5]"),
    ("confidence label", r"(?i)\bconfidence:\s*(high|medium|low)\b"),
    ("doc quality grade", r"\b(RICH|MODERATE|THIN)\s*\(\d"),
    ("corrections language", r"(?i)\b(we previously|we had (this )?wrong|earlier research (said|stated)|correction \d|contradictions? (with|to) the brief|imported error|overturn)"),
    ("open items section", r"(?i)^#+\s*open items"),
    ("research tooling", r"(?i)\b(perplexity|sonar|openrouter|rwa\.xyz metadata|research agent|wave 1|wave 2)\b"),
    ("internal process ref", r"(?i)\b(B\d\b|Phase [0-9]|the brief\b|working notes|handoff|MD blueprint)"),
    ("section symbol", r"§"),
    ("ai tell", r"(?i)\b(delve|delves|delving|in the realm of|navigate the complexities|stands as a testament|a testament to|underscores|pivotal|crucial|seamless|comprehensive suite|at its core|when it comes to|it'?s important to note|it is important to note)\b"),
    ("ai tell: landscape of", r"(?i)\blandscape of\b"),
    ("ai tell: robust", r"(?i)\brobust\b"),
    ("ai tell: leverage verb", r"(?i)\b(leverages|leveraging|to leverage)\b"),
    ("not just X but Y", r"(?i)not just [^.,;]{2,40}, but"),
    ("filler opener", r"(?im)^(Moreover|Furthermore|Additionally|Notably),"),
]

def main():
    total = 0
    for name in FILES:
        path = os.path.join(W, name)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8-sig") as f:
            lines = f.read().replace("\r\n", "\n").split("\n")
        hits = []
        for label, pat in CHECKS:
            rx = re.compile(pat, re.M)
            for i, line in enumerate(lines, 1):
                for m in rx.finditer(line):
                    ctx = line.strip()
                    hits.append((label, i, m.group(0), ctx[:130]))
        if hits:
            print("\n=== %s (%d) ===" % (name, len(hits)))
            for label, i, tok, ctx in hits[:60]:
                print("  L%-5d %-24s %-22r %s" % (i, label, tok, ctx))
            if len(hits) > 60:
                print("  ... %d more" % (len(hits) - 60))
        total += len(hits)
    print("\nTOTAL: %d" % total)
    return 0

if __name__ == "__main__":
    sys.exit(main())
