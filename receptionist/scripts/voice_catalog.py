"""Voice catalog loader. Reads workspace voice-catalog.json keyed by industry.

The catalog lives in the client-fulfillment ICM workspace (single canonical home).
This module reads it at runtime so production provisioning matches the documented
mapping. If the catalog cannot be found (workspace renamed / moved), falls back
to the historical legacy voice ID and prints a warning.

Origin: D6 patch 2026-05-20. See
`jake-van-clief-icm/workspaces/client-fulfillment/D6-setup-new-client-patch-PROPOSAL.md`.
"""

from __future__ import annotations
import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Mapping, TypedDict


_WORKSPACE_DEFAULT = Path(
    "C:/Users/a33_s/Desktop/claude MCPs/New repos/jake-van-clief-icm/workspaces"
    "/client-fulfillment/03a-receptionist-build/references/voice-catalog.json"
)


class VoiceEntry(TypedDict):
    voice_id: str
    voice_name: str
    source: str


_LEGACY_FALLBACK: VoiceEntry = {
    "voice_id": "dN8hviqdNrAsEcL57yFj",
    "voice_name": "(legacy fallback)",
    "source": "in-code legacy",
}

# business_type keyword -> canonical catalog key. Mirrors capture_lead pattern
# (see claude-mem obs 11334, 11338, 21920 — keep this in lockstep with
# server.py /capture-lead routing or Claire's transfer and the voice will
# disagree). SINGLE-WORD TOKENS ONLY — \b boundaries break on multi-word keys.
_BUSINESS_TYPE_SYNONYMS: Mapping[str, str] = {
    # dental + medical (capture_lead routes clinic/medical/health to dental too)
    "dental": "dental", "dentist": "dental", "orthodontist": "dental",
    "clinic": "dental", "medical": "dental", "health": "dental",
    # motor factors / garage / mechanic
    "motor": "motor_factors", "garage": "motor_factors", "mechanic": "motor_factors",
    "parts": "motor_factors", "factors": "motor_factors",
    # salon / hair / beauty / barber
    "salon": "salon", "hair": "salon", "beauty": "salon", "barber": "salon",
    # solicitor / law
    "solicitor": "solicitor", "legal": "solicitor", "law": "solicitor",
    # restaurant / cafe / takeaway / pub / bistro
    "restaurant": "restaurant", "cafe": "restaurant", "bistro": "restaurant",
    "takeaway": "restaurant", "pub": "restaurant",
}


def _normalise_vertical(industry: str | None, business_type: str | None) -> str:
    """Map freeform business_type OR canonical industry to a catalog key."""
    if industry:
        return industry.strip().lower() or "default"
    if not business_type:
        return "default"
    bt = business_type.strip().lower()
    if bt in _BUSINESS_TYPE_SYNONYMS:
        return _BUSINESS_TYPE_SYNONYMS[bt]
    for token, canonical in _BUSINESS_TYPE_SYNONYMS.items():
        if re.search(rf"\b{re.escape(token)}\b", bt):
            return canonical
    return "default"


@lru_cache(maxsize=1)
def _load_catalog() -> dict[str, VoiceEntry]:
    # Lookup precedence: explicit env var > Render-side sibling mirror >
    # workspace canonical (dev). Strategy A copies the workspace JSON to the
    # sibling path at commit time so Render deploys ship with it.
    sibling = Path(__file__).parent / "voice-catalog.json"
    override = os.environ.get("CALLMEIE_VOICE_CATALOG")
    path = Path(override) if override else (sibling if sibling.exists() else _WORKSPACE_DEFAULT)
    if not path.exists():
        print(f"[voice_catalog] WARNING: {path} not found; using legacy fallback")
        return {"default": _LEGACY_FALLBACK}
    return json.loads(path.read_text(encoding="utf-8"))["vertical_voice_map"]


def refresh() -> None:
    """Clear the lru_cache. Required by tests; useful for long-running processes
    that edit the catalog in-place (server.py reloads on Render redeploy only)."""
    _load_catalog.cache_clear()


def voice_for_industry(
    industry: str | None = None,
    business_type: str | None = None,
) -> VoiceEntry:
    """Return voice entry for a vertical.

    Accepts canonical `industry` (e.g. from client.json) OR freeform `business_type`
    (e.g. from onboard form). Falls through to 'default' if neither maps.
    """
    catalog = _load_catalog()
    key = _normalise_vertical(industry, business_type)
    return catalog.get(key, catalog.get("default", _LEGACY_FALLBACK))
