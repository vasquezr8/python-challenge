import os
import csv

with open("budget_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_profit_losses = 0
    total_months = 0

    sum_profit_losses = 0

    # Add up profit/losses
    for row in csvreader:

        profit_losses = row[1]

        total_profit_losses = total_profit_losses + profit_losses
        total_months = total_months + 1

        if total_months > 1:
            change = profit_losses - last_profit_losses

            sum_profit_losses = sum_profit_losses + change

        last_profit_losses = row[1]

    # Summary table outside of loop
    print("Financial Analysis")
    print("----------------------------")

    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: $({sum_profit_losses} / ({total_months} - 1))")