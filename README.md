1. ✅ **How the code is organized**

* You have a **Project Structure** section listing files and their purposes.

2. ✅ **Instructions on how to install dependencies and execute the program**

* You provide installation steps using **Poetry**, and include an example usage.

3. ✅ **Mention any tools (e.g., LLMs or libraries) used**

* You list **Python**, **Poetry**, **Requests**, and **PubMed API**, each with appropriate links.

---

⚠️ Small Enhancements Suggested:

* Add **direct links to each script** in the GitHub repo.
* Clarify that the program uses **heuristics**, not a true **LLM**, for non-academic author detection (important if you're being evaluated on "tool usage").

---

✅ Final Corrected and Enhanced `README.md`

```markdown
# PaperFetch

**PaperFetch** is a command-line tool written in Python for fetching research paper metadata from PubMed using their E-Utilities API. It flags potential non-academic authors using affiliation-based heuristics.

---

## 📁 Code Organization

```

.
├── fetch.py               # Fetches paper IDs using PubMed API and query
├── fetch\_details.py       # Retrieves metadata (title, date, authors, etc.)
├── get\_papers.py          # Main script that ties fetching and saving CSV
├── results.csv            # Output file (auto-generated)
├── pyproject.toml         # Poetry dependency config
├── README.md              # This file (documentation)

````

---

## 🧪 Installation

### Requirements:
- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation)

### Steps:
```bash
# 1. Clone the repository
git clone https://github.com/Abinaya-2601/paperfetch.git
cd paperfetch

# 2. Install dependencies
poetry install
````

---

▶️ How to Run

```bash
# Basic query to fetch papers and save results
poetry run get-papers-list "your search term here" -f results.csv
```

CLI Options:

| Option          | Description                                   |
| --------------- | --------------------------------------------- |
| `-h`, `--help`  | Show help message                             |
| `-d`, `--debug` | Enable debug logs                             |
| `-f`, `--file`  | Output CSV file name (default: `results.csv`) |

---

🧠 Non-Academic Author Detection Logic

This tool **does not use an LLM**, but uses rule-based heuristics to detect non-academic authors:

A name is considered **non-academic** if:

* The affiliation is missing or undefined
* OR it lacks keywords like:

  * `university`, `college`, `institute`, `school`, `hospital`

Such names are listed in the `Non-academic Authors` column in the output CSV.

---

🛠️ Tools & Libraries Used

| Tool/Library                                                           | Purpose                    | Link |
| ---------------------------------------------------------------------- | -------------------------- | ---- |
| [Python 3.11+](https://www.python.org/downloads/)                      | Core language              |      |
| [Poetry](https://python-poetry.org/)                                   | Dependency and packaging   |      |
| [Requests](https://pypi.org/project/requests/)                         | HTTP requests to PubMed    |      |
| [PubMed E-Utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25500/) | Source of publication data |      |

---

📄 Output Format (CSV)

The program outputs results in the following structure:

| PubMedID | Title | Publication Date | Non-academic Authors |
| -------- | ----- | ---------------- | -------------------- |
| ...      | ...   | ...              | Author1; Author2     |

---

## 👩‍💻 Author

Abinaya B
Sri Sairam Engineering College
B.Tech CSE (IoT) | Batch 2022–2026

---
