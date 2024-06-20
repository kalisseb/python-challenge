import os
import csv

b_data = "./Resources/budget_data.csv"
with open (b_data, "r") as file:
    with open ("./analysis/analysis.txt", "w") as export:
        reader = csv.reader(file)
        next(reader)