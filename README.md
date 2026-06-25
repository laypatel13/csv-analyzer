# 📊 CSV Analyzer - CLI
A simple command-line CSV Analyzer built using Python. This project helps you analyze CSV files and view column-wise statistics with a colorful and neatly formatted tabular interface.

---

## ✨ Features

- Analyze any CSV file for numeric column statistics
- Displays Mean, Min, Max, and Std Dev per column
- Skips non-numeric columns gracefully
- Export analysis report to a `.txt` file
- Colorful CLI output for better readability

---

## 📦 Install via pip

```bash
pip install laypatel13-csv-analyzer
```

Then run it from anywhere in your terminal:

```bash
csv-analyzer
```

---

## 🛠️ Install from source

```bash
git clone https://github.com/laypatel13/csv-analyzer.git
cd csv-analyzer
pip install -r requirements.txt
pip install -e .
```

Then run:

```bash
csv-analyzer
```

---

## 📂 Project Structure

```text
csv-analyzer/
├── csv_analyzer/
│   ├── __init__.py
│   └── main.py
├── sample-data.csv
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧰 Built With

- Used [NumPy](https://numpy.org/) for statistical computations.
- Used [Colorama](https://pypi.org/project/colorama/) for colored terminal output.
- Used [Tabulate](https://pypi.org/project/tabulate/) for formatted table display.