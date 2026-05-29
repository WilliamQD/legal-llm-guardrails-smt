"""Schema validation for private preference records.

The public repo does not include training examples. This module documents and
checks the record contract used by the private LoRA fine-tuning workflow.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping


REQUIRED_KEYS = {"prompt", "chosen", "rejected"}


def validate_preference_records(records: Iterable[Mapping[str, str]]) -> list[str]:
    """Return validation errors for preference-style records.

    A valid record contains exactly ``prompt``, ``chosen``, and ``rejected``.
    Both answers must start with ``Verdict:`` so downstream evaluation can parse
    them reliably.
    """

    errors: list[str] = []
    for index, record in enumerate(records, start=1):
        keys = set(record)
        if keys != REQUIRED_KEYS:
            errors.append(
                f"record {index}: expected keys {sorted(REQUIRED_KEYS)}, got {sorted(keys)}"
            )
            continue

        for field in ("prompt", "chosen", "rejected"):
            value = record[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"record {index}: {field} must be a non-empty string")

        for field in ("chosen", "rejected"):
            value = record[field]
            if isinstance(value, str) and not value.startswith("Verdict:"):
                errors.append(f"record {index}: {field} must start with 'Verdict:'")

    return errors
