Term Project Report: Using SMT for Guardrailing LLMs
William Zhang
Course: CPSC 4151
Date: April 25, 2026

Setup:

Questions:
1. Dataset ablation: the 10-example and 20-example adapters performed identically on the six held-out cases, each with 3 Correct, 2 Error, and 1 Ambiguous. The 50-example adapter performed slightly worse with 2 Correct, 3 Error, and 1 Ambiguous, because it flipped the aunt scenario from a correct Yes to an incorrect No while still missing the same two No cases. More data therefore did not consistently help here. The medium dataset gave no improvement over the small one, and the large dataset did not help on the harder borderline cases.

2. Method justification: I chose LoRA instead of DPO because the datasets were small and I wanted a simpler, more reproducible training setup for HPC. LoRA also made it easier to compare three dataset sizes without changing the learning method. The tradeoff is that DPO would have used the preference structure more directly, while my pipeline used the `chosen` answers for supervised fine-tuning and kept the `rejected` answers mainly for dataset design and later error analysis.

3. Model behavior: the clearest strength was handling obvious qualifying-child cases such as James and Sophie, and the small and medium adapters also got the aunt scenario right. The main weakness was overpredicting dependency. All three models answered Yes for Linda and Carlos even though the SMT formalization returned No, which suggests weak handling of the gross-income threshold and the age or student cutoff. The Maria case also showed weak ambiguity handling, since every model forced a Yes answer even though the SMT result was intentionally unresolved. The raw explanations often sounded confident while inventing relationships or unsupported legal details. The dataset was built from SMT-checked variants of earlier scenarios plus manual examples covering missing rule combinations, with each `chosen` answer intended to match the project's legal classification and each `rejected` answer written to be plausible but wrong or incomplete.
