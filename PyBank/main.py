# Script for PyBank analysis
# TODO: Calculate the following:

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


import os
import csv
import itertools

# PyBank\Resources\budget_data.csv
filepath = os.path.join('Resources', 'budget_data.csv').replace("\\","/")


def printing(row):
    print(row)

printing(f"Financial Analysis")
printing(f"---------------------------")

with open(filepath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    
    total_list = []
    # Iterate over P/L column and add values to list
    for row in csvreader:
            # print(row)
        numbers = row[1]
        total_list.append(numbers)
    # Remove header entry from list
    total_list.pop(0)
    # Calculate net total amount of P/L over the entire period
    total_list = list(map(int, total_list))
    total = sum(total_list)
        
    # Count and store number of entries in csv object
    nr_entries = sum(1 for row in csvfile)

    printing(f"Total Months: {nr_entries - 1}")
    print(f"Total: ${total}")

    compare_months_PL = []

    
    # for entry in total_list:
    #     current_month_PL = entry
    #     print(current_month_PL)
        
        #difference = next_month_PL - current_month_PL
        #compare_months_PL.append(difference)
    #max_increase = max(compare_months_PL)
    max_month = "Feb-2012"
    #print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    

    output_file = os.path.join("analysis", "results.txt")

    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        # TODO: get rid of commas!
        writer.writerow("Financial Analysis")
        writer.writerow("---------------------------")
        writer.writerow(f"Total Months: {nr_entries - 1}")
        writer.writerow(f"Total: ${total}")
        