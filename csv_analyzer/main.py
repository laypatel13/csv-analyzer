import numpy as np
import os
import csv
from colorama import init, Fore, Back, Style
from tabulate import tabulate

init(autoreset=True)

def load_csv(filename):
    if not os.path.exists(filename):
        print(Fore.WHITE + Back.RED + "Fatal Error: File Not Found!" + Style.RESET_ALL)
        return None, None
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
    except IOError as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed to load file. {e}" + Style.RESET_ALL)
        return None, None

    header = rows[0]
    data = rows[1:]
    return header, data

def analyze(data, headers):
    table_data = []
    skipped = []

    for i, col_name in enumerate(headers):
        try:
            column = np.array([float(row[i]) for row in data])
            table_data.append([
                Fore.WHITE + Style.BRIGHT + col_name + Style.RESET_ALL,
                Fore.WHITE + Style.NORMAL + f"{np.mean(column):.2f}" + Style.RESET_ALL,
                Fore.WHITE + Style.NORMAL + f"{np.min(column):.2f}" + Style.RESET_ALL,
                Fore.WHITE + Style.NORMAL + f"{np.max(column):.2f}" + Style.RESET_ALL,
                Fore.WHITE + Style.NORMAL + f"{np.std(column):.2f}" + Style.RESET_ALL,
            ])
        except ValueError:
            skipped.append(col_name)

    headers_row = [
        Style.BRIGHT + "Column" + Style.RESET_ALL,
        Style.BRIGHT + "Mean" + Style.RESET_ALL,
        Style.BRIGHT + "Min" + Style.RESET_ALL,
        Style.BRIGHT + "Max" + Style.RESET_ALL,
        Style.BRIGHT + "Std Dev" + Style.RESET_ALL,
    ]

    print(tabulate(table_data, headers=headers_row, tablefmt="pretty", disable_numparse=True))

    if skipped:
        for col in skipped:
            print(Fore.YELLOW + f"  '{col}' skipped (not numeric)" + Style.RESET_ALL)

def export_report(data, headers, source_filename):
    lines = []
    lines.append("--- CSV Analysis Report ---\n")
    lines.append(f"Source: {source_filename}\n\n")

    for i, col_name in enumerate(headers):
        try:
            column = np.array([float(row[i]) for row in data])
            lines.append(f"{col_name.upper()}\n")
            lines.append(f"  Mean   : {np.mean(column):.2f}\n")
            lines.append(f"  Min    : {np.min(column):.2f}\n")
            lines.append(f"  Max    : {np.max(column):.2f}\n")
            lines.append(f"  Std Dev: {np.std(column):.2f}\n\n")
        except ValueError:
            lines.append(f"{col_name.upper()} - skipped (not numeric)\n\n")

    output_file = source_filename.replace(".csv", "_report.txt")
    try:
        with open(output_file, "w") as f:
            f.writelines(lines)
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"Report saved to {output_file}!" + Style.RESET_ALL)
    except IOError as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed to save report. {e}" + Style.RESET_ALL)

def main():
    filename = input(Fore.CYAN + Style.BRIGHT + "Enter CSV filename: " + Style.RESET_ALL)
    headers, data = load_csv(filename)
    if data is None:
        return

    print("\n" + Fore.BLACK + Back.WHITE + "--- CSV Analysis Report ---" + Style.RESET_ALL)
    analyze(data, headers)

    export = input("\n" + Fore.CYAN + Style.BRIGHT + "Export report to txt file? (yes/no): " + Style.RESET_ALL)
    if export.lower() == "yes":
        export_report(data, headers, filename)

if __name__ == "__main__":
    main()
