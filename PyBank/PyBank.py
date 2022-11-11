# Modules
import os
import csv
import statistics
#Define variables
total_months = []
period_change = []
profit_loss_amount = []
rev = []
changes = []
change_list = []
total_rev = 0
greatest_increase = ["", 0]
greatest_decrease = ['', 999999999999999999]
best = ''
worst = ''
month_count = 0
# Read csv
csvpath = os.path.join("budget_data.csv")
out_file = os.path.join("open.txt")
with open("budget_data.csv") as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)
    csv_first = next(csvreader)
    # print(csv_first)
    previous = int(csv_first[1])
    month_count += 1
    total_rev += int(csv_first[1])

    for row in csvreader:
    # Total months
        total_months.append(row[0])
        month_count += 1
        total_rev += int(row[1])

        # Greatest Increase and Decrease
        
        x = int(row[1]) - previous
        previous = int(row[1])
        change_list = change_list + [x]
        period_change = period_change + [row[0]]

        if x > greatest_increase[1]:
            # best = (row[0])
            greatest_increase[0] = (row[0])
            greatest_increase[1] = x
        elif x < greatest_decrease[1]:
            # worst = (row[0])
            greatest_decrease[0] = ((row[0]))
            greatest_decrease[1] = x
    average_change = round(statistics.mean(change_list),2)
       
    # print(month_count)
    # print(total_rev)
    # print(average_change)

# Print Statements
output = (
    f"Financial Analysis \n"
    f"---------------------------- \n"
    f"Total Months: {month_count} \n"
    f"Total: $ {total_rev} \n"
    f"Average Change: $ {average_change} \n"
    f"Greatest Increase in Profits:  {greatest_increase} \n"
    f"Greatest Decrease in Profits: {greatest_decrease} \n"
)
print(output)
with open(out_file, "w") as outfile:
    outfile.write(output)