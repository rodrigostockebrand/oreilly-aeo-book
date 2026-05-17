# Answer Engine Optimization (AEO) — O'Reilly Book

Companion code repository for the upcoming O'Reilly book on **Answer Engine Optimization (AEO)** by **Rodrigo Stockebrand**.

This repo contains the full versions of code samples, JSON-LD snippets, and Python utilities that are abbreviated in the printed book to save space.

## How to use this repo

Each chapter has its own folder (e.g., `chapter-03/`) with subfolders by script type:

```
chapter-NN/
├── python/      # Python scripts (crawlers, analyzers, API clients)
├── json-ld/     # Structured data examples
├── js/          # JavaScript / browser snippets
├── html/        # Markup examples
├── data/        # Sample input/output data
└── README.md    # Chapter-specific notes and run instructions
```

## Chapters

| Chapter | Title | Folder |
|---|---|---|
| 3 | _(TBD)_ | [`chapter-03/`](chapter-03/) |

## Running the Python examples

Most Python scripts target **Python 3.10+**. From inside a chapter folder:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # if present
python python/<script_name>.py
```

## License

Code samples are released under the [MIT License](LICENSE) for readers to adapt freely in their own AEO work. The book text itself is © Rodrigo Stockebrand / O'Reilly Media and is **not** included in this repository.

## Errata & feedback

If you find a bug in a code sample, please open an issue or submit a pull request. Errata for the book text should be reported through O'Reilly's official channels.

---

**Author:** Rodrigo Stockebrand
**Publisher:** O'Reilly Media
