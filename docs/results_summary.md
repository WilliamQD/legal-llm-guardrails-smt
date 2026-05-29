# Results Summary

The final project compared three LoRA adapters trained on different dataset sizes.

| Adapter | Correct | Error | Ambiguous |
|---|---:|---:|---:|
| 10 examples | 3 | 2 | 1 |
| 20 examples | 3 | 2 | 1 |
| 50 examples | 2 | 3 | 1 |

## Main Takeaways

More examples did not automatically improve rule-following behavior. The 50-example adapter performed slightly worse on the held-out set because it flipped one previously correct case while still missing the same hard negative cases.

The most consistent failure mode was over-predicting dependency. Model explanations often sounded confident while missing thresholds involving gross income, student status, age cutoffs, or support tests.

The key engineering lesson was that a formal checker can reveal hidden reasoning failures that are easy to miss when evaluating only the fluency of generated explanations.
