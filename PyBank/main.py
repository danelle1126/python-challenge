import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

# initialize variables
TotalMonths = 0
ProfitLoss = 0
InitialProfit = 0
AvgPLChange = 0
GreatestIncrease = 0
GreatestDecrease = 0
LastProfit = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) 
    for row in csvreader:

        # Count months in data
        TotalMonths = TotalMonths + 1

        # Sum total profits and losses
        ProfitLoss = ProfitLoss + int(row[1])

        # Calculate average change in profits and losses
        if TotalMonths == 1:
            InitialProfit = float(row[1])
        if TotalMonths > 1:
            AvgPLChange = (float(row[1]) - InitialProfit) / (TotalMonths - 1)

            # Track greatest monthly increase and decrease in profits and losses
            if (int(row[1]) - LastProfit) > GreatestIncrease:
                GreatestIncrease = int(row[1]) - LastProfit
                GrIncDate = row[0]
            if (int(row[1]) - LastProfit) < GreatestDecrease:
                GreatestDecrease = int(row[1]) - LastProfit
                GrDecDate = row[0]
        LastProfit = int(row[1])     

# print results
print("Financial Analysis")
print("----------------------------------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total Profit: ${ProfitLoss:,}")
print(f"Average Change: ${AvgPLChange:,.2f}")   
print(f"Greatest Increase in Profits: {GrIncDate} ${GreatestIncrease:,}")    
print(f"Greatest Decrease in Profits: {GrDecDate} ${GreatestDecrease:,}") 

# export results to text file
output_path = os.path.join("Analysis","output.txt")
with open(output_path,'w',newline='') as text_file:
    text_file.write("Financial Analysis \n")
    text_file.write("---------------------------------------------------- \n")
    text_file.write(f"Total Months: {TotalMonths} \n")
    text_file.write(f"Total Profit: ${ProfitLoss:,} \n")
    text_file.write(f"Average Change: ${AvgPLChange:,.2f} \n")   
    text_file.write(f"Greatest Increase in Profits: {GrIncDate} ${GreatestIncrease:,} \n")    
    text_file.write(f"Greatest Decrease in Profits: {GrDecDate} ${GreatestDecrease:,} \n") 
