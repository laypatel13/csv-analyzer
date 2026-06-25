from email import header

import numpy as np
import os
import csv

def load_csv(filename):
    if not os.path.exists(filename):
        print("File Not Found!")
        return None, None
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]

    return header, data

def analyze(data, headers):
    for i, col_name in enumerate(headers): 
        try:
            column = np.array([float(row[i]) for row in data])
            print(f"\n{col_name.upper()}")
            print(f"  Mean   : {np.mean(column):.2f}")
            print(f"  Min    : {np.min(column):.2f}")
            print(f"  Max    : {np.max(column):.2f}")
            print(f"  Std Dev: {np.std(column):.2f}")
        except ValueError:
            print(f"\n{col_name.upper()} - skipped (not numeric)")


def main():
    filename = input("Enter CSV filename: ")
    headers, data = load_csv(filename)
    if data is None:
        return
    print("\n--- CSV Analysis Report ---")
    analyze(data, headers)

if __name__ == "__main__":
    main()