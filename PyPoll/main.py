# Script for PyPoll analysis
import os
import csv
from decimal import *


# Set file path to budget data: PyBank\Resources\budget_data.csv
filepath = os.path.join('Resources', 'election_data.csv').replace("\\","/")

# Print headers for output
print(f"Election Results")
print(f"---------------------------")

with open(filepath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Make list to count and store number of entries in csv object
    csv_list = list(csvreader)
    nr_entries = len(csv_list)
       
    vote_list = []
    # Iterate over P/L column and add values to list
    for item in csv_list:
        vote = item[0]
        vote_list.append(vote)
    # Remove header entry from list
    vote_list.pop(0)
    # Calculate the total number of votes cast
    total = len(vote_list)
    print(f"Total Votes: {total}")
    print(f"---------------------------")

    # Generate a complete list of candidates who received votes
    candidates_list = []
    # Iterate over P/L column and add values to list
    for item in csv_list:
        candidate = item[2]
        candidates_list.append(candidate)
    # Remove header entry from list
    candidates_list.pop(0)

    # function to get unique values 
    def unique(list): 
        # intilize a null list 
        unique_candidates_list = []    
        # traverse for all elements 
        for name in list: 
            # check if exists in unique_list or not 
            if name not in unique_candidates_list: 
                unique_candidates_list.append(name) 
        return unique_candidates_list
    
    candidates = []
    candidates = unique(candidates_list) 

    # Write results to text file in analysis folder
    output_file = os.path.join("analysis", "results.txt")
    
    # Calculate the total number of votes each candidate won
    # Calculate the percentage of votes each candidate won
    candidate_votes = []
    winner_list = []
    output = []
    for name in candidates:
        for item in csv_list:
            vote = item[2]
            if vote == name:
                candidate_votes.append(vote)
        
        total_votes_candidate = (len(candidate_votes))
        winner_list.append(total_votes_candidate)
        # winning_votes = 0
        # if total_votes_candidate > winning_votes:
        #     winning_votes = total_votes_candidate
        #     winner = name

        # Set precision of voting results to 5 decimal places
        getcontext().prec = 5
        votes_candidate_percent = (Decimal(total_votes_candidate) / Decimal(nr_entries)) *100
        print(f"{name}: {votes_candidate_percent}%  ({total_votes_candidate})")
        output.append(f"{name}: {votes_candidate_percent}%  ({total_votes_candidate})")
        candidate_votes = []
    
    # Calculate the winner of the election based on popular vote.
    winner = max(winner_list)

    print(f"---------------------------")
    print(f"Winner: {winner}")
    print(f"---------------------------")
      
    # 
    # 
    # winner_list.append(total_votes_correy)
    # winner_list.append(total_votes_li)
    # winner_list.append(total_votes_otooley)

    # 

    # if winner == total_votes_otooley:
    #     winner_name = "O'Tooley"
    # elif winner == total_votes_correy:
    #     winner_name = "Correy"
    # elif winner == total_votes_khan:
    #     winner_name = "Khan"
    # else:
    #     winner_name = "Li"
   
    # Calculate greatest increase in profits (date and amount) over the entire period
    # greatest_increase = max(difference)
    # greatest_inc_moyr = dictionary.get(greatest_increase)
    # print(f"Greatest Increase in Profits: {greatest_inc_moyr} (${greatest_increase})")
   
    
    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        # TODO: get rid of line breaks?
        writer.writerow(["Election Results"])
        writer.writerow(["---------------------------"])
        writer.writerow([f"Total Votes: {total}"])
        writer.writerow(["---------------------------"])
        for candidate_stats in output:
            writer.writerow([candidate_stats])
        writer.writerow(["---------------------------"])
        #writer.writerow([f"Winner: {winner}"])
        writer.writerow(["---------------------------"])