from asyncore import read
from functools import total_ordering
import os
import csv
#Read CSV file
budget_csv = os.path.join("Resources","budget_data.csv")
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    header_row = next(csv_reader,None)
    #Set variables and lists to 0
    months = []
    profit_loss_changes = []
    rowcount = 0
    total = 0
    curr_month = 0
    prev_month = 0
    change_profit_loss = 0
    # Iterate through rows and store data in lists
    for row in csv_reader:
        rowcount +=1
        total += int(row[1])
        curr_month = int(row[1])
        if rowcount == 1:
            prev_month += curr_month
        else:
            change_profit_loss = curr_month - prev_month
            prev_month = curr_month
            #Store results
            months.append(row[0])
            profit_loss_changes.append(change_profit_loss )

    #Calculate Analysis
    average = round(sum(profit_loss_changes)/(rowcount-1),2)
    max_increase = max(profit_loss_changes)
    min_increase = min(profit_loss_changes)
    max_index = profit_loss_changes.index(max_increase)
    min_index = profit_loss_changes.index(min_increase)
    max_month = months[max_index]
    min_month = months[min_index]
    #Print on terminal
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months:", rowcount)
    print("Total: $",total)
    print("Average: $",round(average,2))
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Increase in Profits: {min_month} (${min_increase})")
    
   #Export to txt file
    txt_path = os.path.join("Analysis", "Financial_Analysis.txt")
    f = open(txt_path, "x")
    f.write("Financial Analysis\n")
    f.write("-------------------------\n")
    f.write(f"Total Months: {rowcount}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average: ${average}\n")
    f.write(f"Greatest Increase in Profits: {max_month} (${max_increase})\n")
    f.write(f"Greatest Increase in Profits: {min_month} (${min_increase})")
    f.close()