"""Markdown summaries for model-vs-SMT comparisons."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping


def summarize_statuses(rows: Iterable[Mapping[str, str]]) -> Counter[str]:
    """Count evaluation statuses."""

    return Counter(row["status"] for row in rows)


def build_summary_table(title: str, rows: Iterable[Mapping[str, str]]) -> str:
    """Build a Markdown table for public-safe aggregate or synthetic rows."""

    lines = [
        f"# {title}",
        "",
        "| Fact Pattern | Model Output | SMT Verdict | Status |",
        "|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {fact_pattern} | {model_verdict} | {smt_verdict} | {status} |".format(
                fact_pattern=row["fact_pattern"],
                model_verdict=row["model_verdict"],
                smt_verdict=row["smt_verdict"],
                status=row["status"],
            )
        )
    return "\n".join(lines) + "\n"
