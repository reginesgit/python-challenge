# Script for PyBank analysis
import os
import csv

# Set file path to budget data: PyBank\Resources\budget_data.csv
filepath = os.path.join('Resources', 'budget_data.csv').replace("\\","/")

# Print headers for output
print(f"Financial Analysis")
print(f"---------------------------")

with open(filepath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Make list to count and store number of entries in csv object
    csv_list = list(csvreader)
    nr_entries = len(csv_list)
    print(f"Total Months: {nr_entries - 1}")
       
    int_PL_list = []
    # Iterate over P/L column and add values to list
    for item in csv_list:
        number = item[1]
        int_PL_list.append(number)
    # Remove header entry from list
    int_PL_list.pop(0)
    # Convert list to int, then
    # Calculate net total amount of P/L over the entire period
    int_PL_list = list(map(int, int_PL_list))
    total = sum(int_PL_list)
    print(f"Total: ${total}")

    # Calculate the changes in "Profit/Losses" over the entire period, 
    # then find the average of those changes
    first_mo_PL = int_PL_list[0]
    last_mo_PL = int_PL_list[85]
    average = (last_mo_PL - first_mo_PL) / 85    
    rounded_average = round(average, 2)
    print(f"Average Change : ${rounded_average}")

    # Copy P/L list and remove first value to get next month's P/L
    int_next_mos_PL_list = int_PL_list.copy()
    int_next_mos_PL_list.pop(0)
    # Make new list to store the difference between current and next months' P/L
    difference = []
    zip_lists = zip(int_PL_list, int_next_mos_PL_list)
    for int_PL_list_x, int_next_mos_PL_list_y in zip_lists:
        difference.append(int_next_mos_PL_list_y - int_PL_list_x)
    # Make new list for months to match max./min. P/L to
    month_list = []
    # Iterate over Date column and add values to list
    for item in csv_list:
        month = item[0]
        month_list.append(month)
    # Remove first two entries to reflect correct change month
    month_list.pop(0)
    month_list.pop(0)
    # Create a dictionary of key = P/L and value = Date
    zip_differences = zip(difference, month_list)
    dictionary = dict(zip_differences)
        
    # Calculate greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(difference)
    greatest_inc_moyr = dictionary.get(greatest_increase)
    print(f"Greatest Increase in Profits: {greatest_inc_moyr} (${greatest_increase})")
          
    # The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(difference)
    greatest_dec_moyr = dictionary.get(greatest_decrease)
    print(f"Greatest Decrease in Profits:  {greatest_dec_moyr} (${greatest_decrease})")

    # Write results to text file in analysis folder
    output_file = os.path.join("analysis", "results.txt")

    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Financial Analysis"])
        writer.writerow(["---------------------------"])
        writer.writerow([f"Total Months: {nr_entries - 1}"])
        writer.writerow([f"Total: ${total}"])
        writer.writerow([f"Average Change : ${rounded_average}"])
        writer.writerow([f"Greatest Increase in Profits: {greatest_inc_moyr} (${greatest_increase})"])
        writer.writerow([f"Greatest Decrease in Profits: {greatest_dec_moyr} (${greatest_decrease})"])
        