import csv
import os

# Variables and Lists for dates/months, profit/loss values, and overall and row-to-row data.
monthCount = 1 # Initialize monthCount to 1 to account for the first row read separately
totalProfits = 0
dateMonth = [] 
netMOverM = [] 
greatestProfit = ["", 0]
greatestLoss = ["", 999999999999999]

# Read in CSV and separate the header
with open('python-challenge/PyBank/Resources/budget_data.csv', 'r') as csvFile:
    csvRead = csv.reader(csvFile)

    # Identifying the header and then the second row as the first row of data
    header = next(csvRead)
    firstRow = next(csvRead)
    prevProfitLoss = int(firstRow[1])
    totalProfits += prevProfitLoss

    # Processing remaining rows
    for row in csvRead:
        # Total calculations counting the number of months and summing profit/loss values
        monthCount += 1
        currentProfitLoss = int(row[1])
        totalProfits += currentProfitLoss

        # Row-to-row changes between values and calculating month-over-month change
        mOverMChange = currentProfitLoss - prevProfitLoss
        netMOverM.append(mOverMChange)
        dateMonth.append(row[0])

        # Greatest Profit Calculation
        if mOverMChange > greatestProfit[1]:
            greatestProfit[0] = row[0] # Date/Month
            greatestProfit[1] = mOverMChange # Actual greatest profit change value

        # Greatest Loss Calculation
        if mOverMChange < greatestLoss[1]:
            greatestLoss[0] = row[0]
            greatestLoss[1] = mOverMChange

        # Update prevProfitLoss for the next iteration
        prevProfitLoss = currentProfitLoss

# Calculating the average change
monthlyAvg = sum(netMOverM) / len(netMOverM) if netMOverM else 0

# Formatted summary/output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {monthCount}\n"
    f"Total: ${totalProfits}\n"
    f"Average Change: ${monthlyAvg:.2f}\n"
    f"Greatest Increase in Profits: {greatestProfit[0]} (${greatestProfit[1]})\n"
    f"Greatest Decrease in Profits: {greatestLoss[0]} (${greatestLoss[1]})\n"
)

print(output)

outputDirectory = 'python-challenge\\PyBank\\Analysis'
outputFilePath = os.path.join(outputDirectory, 'budget_analysis.txt')

os.makedirs(outputDirectory, exist_ok=True)

with open (outputFilePath, 'w') as file:
    file.write(output)

print(f"Results saved to {outputFilePath}")