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