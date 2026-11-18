# CSV files 

import csv
import os
os.chdir("SE402/Day01")

# make stock.csv (the first line must be the header)
with open("stock.csv", "w", newline="") as f:
    f.write("name,qty\n")
    f.write("Pen,1\n")
    f.write("Book,3\n")
    f.write("Ruler,8\n")

with open("stock.csv", newline="") as f:
    for row in csv.reader(f):
        print(row)

# reading the file using csv.reader
with open("stock.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["qty"], type(row["qty"]))

with open("stock.csv", newline="") as f:
    for row in csv.DictReader(f):
        qty = int(row["qty"])
        print(row["name"], qty)
        if qty < 5:
            print(" low stock!")