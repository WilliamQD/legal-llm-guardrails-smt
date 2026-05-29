# Data Policy

No datasets are published in this repository.

The original course project used private training/evaluation JSON files and held-out legal fact patterns. Those artifacts are intentionally omitted because this repository is a public portfolio showcase, not a full reproducibility archive.

The code is written so a reviewer can inspect the validation and evaluation approach without accessing private data. If adapting this pattern to another project, place private data locally under `data/`; `.gitignore` prevents common JSON/CSV/XLSX data files from being committed.
