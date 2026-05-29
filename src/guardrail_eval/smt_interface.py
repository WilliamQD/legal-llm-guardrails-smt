"""Thin interface for running local SMT files with Z3.

The public repository does not include private SMT cases. This wrapper is kept
to show how solver execution was isolated from model evaluation.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


def run_z3(smt_path: Path, timeout_seconds: int = 20) -> str:
    """Run Z3 on an SMT-LIB file and return the normalized solver status."""

    if not smt_path.exists():
        raise FileNotFoundError(smt_path)

    result = subprocess.run(
        ["z3", str(smt_path)],
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"z3 exited with {result.returncode}")

    first_line = result.stdout.strip().splitlines()[0] if result.stdout.strip() else ""
    if first_line not in {"sat", "unsat", "unknown"}:
        raise RuntimeError(f"unexpected z3 output: {result.stdout[:200]}")
    return first_line


def status_to_verdict(can_prove_yes: str, can_prove_no: str) -> str:
    """Map paired satisfiability checks into a Yes/No/Ambiguous verdict.

    The original project checked whether a dependent verdict and its negation
    were satisfiable under the same facts. If both remain possible, the scenario
    is under-specified and should be treated as ambiguous.
    """

    if can_prove_yes == "sat" and can_prove_no == "unsat":
        return "Yes"
    if can_prove_yes == "unsat" and can_prove_no == "sat":
        return "No"
    if can_prove_yes == "sat" and can_prove_no == "sat":
        return "Ambiguous"
    raise ValueError(
        f"inconsistent solver statuses: yes={can_prove_yes}, no={can_prove_no}"
    )
