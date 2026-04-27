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

def analyze(data, header):
    for i, header in enumerate(header):
        try:
            column = np.array([float(row[i]) for row in data])
            print(f"\n{header.upper()}")
            print(f"  Mean   : {np.mean(column):.2f}")
            print(f"  Min    : {np.min(column):.2f}")
            print(f"  Max    : {np.max(column):.2f}")
            print(f"  Std Dev: {np.std(column):.2f}")
        except ValueError:
            print(f"\n{header.upper()} - skipped (not numeric)")