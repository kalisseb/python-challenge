import csv
import os

budget = os.path.join("Resources", "budget_data.cav")
budget_rev = os.path.join ("analysis", "budget_analysis.txt")

tot_mo = 0
net_prof_loss = 0
ch_prof_loss = []
inc_greatest = ["", 0]
dec_greatest = ["", 99999999999999999999999999]


with open(budget) as bdata:
    reader = csv.reader(bdata)

    header = next(reader)
