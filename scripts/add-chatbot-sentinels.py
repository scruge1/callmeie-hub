"""add-chatbot-sentinels.py — one-shot inserter for COHESION:CHATBOT sentinels.

Scoped to the receptionist vertical pages (Tier 2 of the P3 chatbot rollout).
Inserts a CHATBOT sentinel pair right above the existing WHATSAPP sentinel
on each target page, then expects scripts/inject-cohesion.py to render the
chatbot partial.

Idempotent: skips any page already containing COHESION:CHATBOT-START.
"""
from __future__ import annotations
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Per-page page_context attr value. All four are "receptionist" since the
# CHATBOT system prompt branches on visitor chip answers, not URL slug.
TARGETS: dict[str, str] = {
    "receptionist/dental.html":        "receptionist",
    "receptionist/motor-factors.html": "receptionist",
    "receptionist/salon.html":         "receptionist",
    "receptionist/solicitor.html":     "receptionist",
}

WA_MARKER = "<!-- COHESION:WHATSAPP-START"
CHAT_MARKER = "<!-- COHESION:CHATBOT-START"


def insert_one(path: Path, page_context: str) -> str:
    text = path.read_text(encoding="utf-8")
    if CHAT_MARKER in text:
        return "skip"
    idx = text.find(WA_MARKER)
    if idx == -1:
        return "no-wa-anchor"
    block = (
        f'<!-- COHESION:CHATBOT-START page_context="{page_context}" -->\n'
        f'<!-- COHESION:CHATBOT-END -->\n\n'
    )
    new_text = text[:idx] + block + text[idx:]
    path.write_text(new_text, encoding="utf-8", newline="\n")
    return "wrote"


def main() -> int:
    counts = {"wrote": 0, "skip": 0, "no-wa-anchor": 0, "missing": 0}
    for rel, ctx in TARGETS.items():
        p = REPO_ROOT / rel
        if not p.is_file():
            counts["missing"] += 1
            print(f"  MISSING  {rel}")
            continue
        result = insert_one(p, ctx)
        counts[result] += 1
        print(f"  {result.upper():13} {rel}")
    print(f"\nSummary: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
