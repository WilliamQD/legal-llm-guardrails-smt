from collections import Counter

from guardrail_eval import (
    build_summary_table,
    compute_status,
    parse_verdict,
    summarize_statuses,
    validate_preference_records,
)
from guardrail_eval.smt_interface import status_to_verdict


def test_parse_verdict_normalizes_expected_format():
    assert parse_verdict("Verdict: yes\nReason: synthetic explanation") == "Yes"
    assert parse_verdict("Verdict: No\nReason: synthetic explanation") == "No"
    assert parse_verdict("Verdict: Ambiguous\nReason: facts are incomplete") == "Ambiguous"


def test_parse_verdict_rejects_unstructured_text():
    assert parse_verdict("Probably yes because it sounds reasonable.") == "Unparseable"


def test_compute_status_uses_smt_label_as_source_of_truth():
    assert compute_status("Yes", "Yes") == "Correct"
    assert compute_status("Yes", "No") == "Error"
    assert compute_status("Yes", "Ambiguous") == "Ambiguous"
    assert compute_status("Unparseable", "No") == "Unparseable"


def test_status_to_verdict_maps_paired_solver_checks():
    assert status_to_verdict("sat", "unsat") == "Yes"
    assert status_to_verdict("unsat", "sat") == "No"
    assert status_to_verdict("sat", "sat") == "Ambiguous"


def test_validate_preference_records_enforces_contract():
    records = [
        {
            "prompt": "Synthetic legal fact pattern.",
            "chosen": "Verdict: Yes\nReason: synthetic reason.",
            "rejected": "Verdict: No\nReason: synthetic counterexample.",
        }
    ]
    assert validate_preference_records(records) == []

    bad_records = [{"prompt": "Missing required answer fields."}]
    assert validate_preference_records(bad_records)


def test_build_summary_table_and_counts():
    rows = [
        {
            "fact_pattern": "Synthetic case A",
            "model_verdict": "Yes",
            "smt_verdict": "Yes",
            "status": "Correct",
        },
        {
            "fact_pattern": "Synthetic case B",
            "model_verdict": "Yes",
            "smt_verdict": "No",
            "status": "Error",
        },
    ]

    assert summarize_statuses(rows) == Counter({"Correct": 1, "Error": 1})
    table = build_summary_table("Synthetic Summary", rows)
    assert "Synthetic Summary" in table
    assert "| Synthetic case A | Yes | Yes | Correct |" in table
