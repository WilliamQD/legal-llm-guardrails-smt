"""Verdict parsing and scoring helpers.

The original project evaluated model generations by reducing each answer to a
stable legal verdict, then comparing that verdict with the SMT-derived label.
These helpers keep that public-safe evaluation layer without including any
private scenarios or model outputs.
"""

from __future__ import annotations

import re


VALID_VERDICTS = {"Yes", "No", "Ambiguous"}


def parse_verdict(text: str) -> str:
    """Extract a normalized verdict from model text.

    Expected model format starts with ``Verdict: Yes|No|Ambiguous``. The parser
    is intentionally conservative: unrecognized text is marked unparseable so it
    cannot be silently counted as correct.
    """

    match = re.search(r"Verdict:\s*(Yes|No|Ambiguous)\b", text, flags=re.IGNORECASE)
    if not match:
        return "Unparseable"

    value = match.group(1).lower()
    if value == "yes":
        return "Yes"
    if value == "no":
        return "No"
    return "Ambiguous"


def compute_status(model_verdict: str, smt_verdict: str) -> str:
    """Compare a model verdict with the SMT verdict."""

    if smt_verdict not in VALID_VERDICTS:
        raise ValueError(f"Unexpected SMT verdict: {smt_verdict}")
    if model_verdict == "Unparseable":
        return "Unparseable"
    if smt_verdict == "Ambiguous":
        return "Ambiguous"
    return "Correct" if model_verdict == smt_verdict else "Error"
