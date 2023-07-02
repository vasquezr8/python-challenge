import os
import csv

with open("budget_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_profit_losses = 0
    total_months = 0

    sum_profit_losses = 0

    greatest_increase = 0

    greatest_decrease = 999999999999

    # Add up profit/losses
    for row in csvreader:

        profit_losses = row[1]

        total_profit_losses = total_profit_losses + int(profit_losses)
        total_months = total_months + 1

        if total_months > 1:
            change = int(profit_losses) - int(last_profit_losses)

            sum_profit_losses = sum_profit_losses + change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]


        last_profit_losses = row[1]

    # Summary table outside of loop
    average_change = sum_profit_losses / (total_months - 1)
    rounded_avg = round(average_change, 2)

    print("Financial Analysis")
    print("----------------------------")

    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${rounded_avg}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")