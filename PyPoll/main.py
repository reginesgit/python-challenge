# Script for PyPoll analysis
import os
import csv
from decimal import *
import warnings
warnings.filterwarnings("ignore")


# Set file path to budget data: PyBank\Resources\budget_data.csv
filepath = os.path.join('Resources', 'election_data.csv').replace("\\","/")


# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

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
    
    candidate_votes = []
    for name in candidates:
        for item in csv_list:
            vote = item[2]
            if vote == name:
                candidate_votes.append(vote)
        
        total_votes_candidate = (len(candidate_votes))
        # Set precision of voting results to 5 decimal places
        getcontext().prec = 5
        votes_candidate_percent = (Decimal(total_votes_candidate) / Decimal(nr_entries)) *100
        print(f"{name}: {votes_candidate_percent}%  ({total_votes_candidate})")
        candidate_votes = []
    
    # winning_votes = 0
    # if total_votes_candidate > winning_votes:
    #     winning_votes = total_votes_candidate
    #     winner = name

    print(f"---------------------------")
    #print(f"Winner: {winner}")
    print(f"---------------------------")
      
    
    # khan_list = []
    # for item in csv_list:
    #     vote_khan = item[2]
    #     if vote_khan == 'Khan':
    #         khan_list.append(vote_khan)
    # total_votes_khan = (len(khan_list))
    # # Set precision of voting results to 5 decimal places
    # getcontext().prec = 5
    # votes_khan_percent = (Decimal(total_votes_khan) / Decimal(nr_entries)) *100
    # # print(votes_khan_percent)
    
    # correy_list = []
    # for item in csv_list:
    #     vote_correy = item[2]
    #     if vote_correy == 'Correy':
    #         correy_list.append(vote_correy)
    # total_votes_correy = (len(correy_list))
    # # Set precision of voting results to 5 decimal places
    # getcontext().prec = 5
    # votes_correy_percent = (Decimal(total_votes_correy) / Decimal(nr_entries)) *100
    # # print(votes_correy_percent)

    # li_list = []
    # for item in csv_list:
    #     vote_li = item[2]
    #     if vote_li == 'Li':
    #         li_list.append(vote_li)
    # total_votes_li = (len(li_list))
    # # Set precision of voting results to 5 decimal places
    # getcontext().prec = 5
    # votes_li_percent = (Decimal(total_votes_li) / Decimal(nr_entries)) *100
    # # print(votes_li_percent)

    # otooley_list = []
    # for item in csv_list:
    #     vote_otooley = item[2]
    #     if vote_otooley == "O'Tooley":
    #         otooley_list.append(vote_otooley)
    # total_votes_otooley = (len(otooley_list))
    # # Set precision of voting results to 5 decimal places
    # getcontext().prec = 4
    # votes_otooley_percent = (Decimal(total_votes_otooley) / Decimal(nr_entries)) *100
    # # print(votes_otooley_percent)

    # winner_list = []
    # winner_list.append(total_votes_khan)
    # winner_list.append(total_votes_correy)
    # winner_list.append(total_votes_li)
    # winner_list.append(total_votes_otooley)

    # winner = max(winner_list)

    # if winner == total_votes_otooley:
    #     winner_name = "O'Tooley"
    # elif winner == total_votes_correy:
    #     winner_name = "Correy"
    # elif winner == total_votes_khan:
    #     winner_name = "Khan"
    # else:
    #     winner_name = "Li"
        
    # print(f"Khan: {votes_khan_percent}%  ({total_votes_khan})")
    # print(f"Correy: {votes_correy_percent}%  ({total_votes_correy})")
    # print(f"Li: {votes_li_percent}%  ({total_votes_li})")
    # print(f"O'Tooley: {votes_otooley_percent}%  ({total_votes_otooley})")
    # print(f"---------------------------")
    # print(f"Winner: {winner_name}")
    # print(f"---------------------------")

   
    # Calculate greatest increase in profits (date and amount) over the entire period
    # greatest_increase = max(difference)
    # greatest_inc_moyr = dictionary.get(greatest_increase)
    # print(f"Greatest Increase in Profits: {greatest_inc_moyr} (${greatest_increase})")
   
    # Write results to text file in analysis folder
    output_file = os.path.join("analysis", "results.txt")

    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        # TODO: get rid of line breaks?
        writer.writerow(["Election Results"])
        writer.writerow(["---------------------------"])
        writer.writerow([f"Total Votes: {total}"])
        writer.writerow(["---------------------------"])
        #writer.writerow([f"Khan: {votes_khan_percent}%  ({total_votes_khan})"])
        #writer.writerow([f"Correy: {votes_correy_percent}%  ({total_votes_correy}"])
        #writer.writerow([f"Li: {votes_li_percent}%  ({total_votes_li})"])
        #writer.writerow([f"O'Tooley: {votes_otooley_percent}%  ({total_votes_otooley})"])
        writer.writerow(["---------------------------"])
        #writer.writerow([f"Winner: {winner}"])
        writer.writerow(["---------------------------"])