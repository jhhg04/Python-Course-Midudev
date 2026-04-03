# Python-Course-Midudev  🐍

This repository is my **Python learning portfolio**, built as a long-term course and structured roadmap.

It contains my progress from fundamentals to practical topics, including code examples, exercises, and mini projects. The purpose is to keep a clean, well-organized reference that demonstrates consistent learning, hands-on practice, and improvement over time.

---

## 📌 Repository Highlights

- ✅ Structured lessons (easy to follow)
- ✅ Hands-on exercises per module
- ✅ Practical scripts and real examples
- ✅ Clean folder organization
- ✅ Designed to grow as the course continues

---

## 🗂 Course Structure

Each module is stored in a dedicated folder:

| Module | Topic |
|--------|-------|
| `01_basic` | Hello World, variables, data types, type conversion |
| `02_flow_control` | Conditionals, lists, and exercises |
| `03_loops` | While/for loops, functions |
| `04_logic` | Programming logic + dictionaries |
| `05_regex` | Regular expressions |
| `06_request_ai_dates` | Fetching data, dates/time, intro to classes |
| `07_scraping` | Web scraping fundamentals |

> New modules will be added as I progress.

---

## 🎯 Learning Goals

This repo focuses on building a strong foundation and real coding confidence:

- Writing clean and readable Python code
- Understanding core programming logic
- Working with built-in data structures
- Practicing problem-solving through exercises
- Building reusable scripts and utilities
- Preparing for real-world Python usage (DevOps, automation, data, etc.)

---

## 🛠 Tech & Tools

- **Python 3.10+** (recommended)
- VS Code (recommended)

Optional libraries used in later modules:
- `requests`
- `beautifulsoup4`
- `lxml`

---

## 🐍 Setting Up a Python Virtual Environment

1. Create a virtual environment
Run the following command in your project folder:
    python -m venv .venv

2. Activate the virtual environment
    On Windows (Git Bash / PowerShell):
    source .venv/Scripts/activate
    On macOS / Linux:
    source .venv/bin/activate

After activation, your terminal should show:
    (.venv)

3. Install dependencies
    pip install requests

4. Save dependencies to a file
    pip freeze > requirements.txt

This will generate a requirements.txt file with all installed packages and their versions.

5. Run your Python script
    python 02_requests.py

🔁 Reusing the environment later
    When you return to the project:
    source .venv/Scripts/activate
    pip install -r requirements.txt
    python 02_requests.py

⚠️ Important Notes
    Do not commit the .venv folder to version control
    Add this to your .gitignore:
    .venv/

💡 Summary
    .venv/ → isolated environment
    requirements.txt → dependency list to recreate the environment

---

## 🚀 How to Run

From the repository root:

```bash
python <file_name>.py
