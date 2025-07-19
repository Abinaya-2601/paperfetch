Here's your complete, ready-to-paste `README.md` content:

---

```markdown
# PaperFetch

**PaperFetch** is a Python-based command-line tool for fetching academic paper details from PubMed using its API. It also attempts to flag non-academic authors based on affiliation heuristics.

---

## 📁 Project Structure

```

.
├── fetch.py               # Module to fetch paper IDs from PubMed
├── fetch\_details.py       # Module to fetch metadata of papers
├── get\_papers.py          # Main CLI script
├── results.csv            # Output file (auto-generated)
├── pyproject.toml         # Poetry configuration file
├── README.md              # Project documentation

````

---

## 📦 Installation

Make sure [Poetry](https://python-poetry.org/docs/#installation) is installed.

```bash
# Clone the repository
git clone https://github.com/Abinaya-2601/paperfetch.git
cd paperfetch

# Install dependencies
poetry install
````

---

## ▶️ Usage

```bash
# Example query
poetry run get-papers-list "machine learning" -f results.csv
```

### CLI Options:

| Option          | Description                                   |
| --------------- | --------------------------------------------- |
| `-h`, `--help`  | Show help message                             |
| `-d`, `--debug` | Enable debug logging                          |
| `-f`, `--file`  | Output CSV file name (default: `results.csv`) |

---

## 🧠 How Non-Academic Authors Are Detected

We apply a heuristic rule based on author affiliation:

A name is considered **non-academic** if:

* The affiliation does **not contain** words like `university`, `college`, `institute`, `school`, or `hospital`
* OR the affiliation is **missing or undefined**
* These names are listed under the "Non-academic Authors" column in the CSV output.

---

## 🧰 Tools & Libraries Used

* [Python 3.11+](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/)
* [Requests](https://pypi.org/project/requests/)
* [PubMed E-Utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25500/)

---

## 📄 Output Format (CSV)

| PubMedID | Title | Publication Date | Non-academic Authors |
| -------- | ----- | ---------------- | -------------------- |
| ...      | ...   | ...              | Author1; Author2     |

---

## 🧑‍💻 Author

Abinaya B
Sri Sairam Engineering College
2022–2026 Batch

---
