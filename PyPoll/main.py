from asyncore import read
import os
import csv
from tkinter import X
#Read open and read CSV file
election_csv = os.path.join("Resources","election_data.csv")

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    header_row = next(csv_reader,None)
    #Set variables and lists to 0
    candidates = []
    percentage = []
    votes = []
    unique_candidates = []
    votecount = 0
    # Iterate through rows and store data in lists
    for row in csv_reader:
        votecount +=1
        candidates.append(row[2])
    for x in set(candidates):
        unique_candidates.append(x)
        votes_per_candidate = candidates.count(x)
        votes.append(votes_per_candidate)
        per = (votes_per_candidate/votecount)*100
        percentage.append(per)
    # Results calculations
    max_votes = max(votes)
    index = votes.index(max_votes)
    winner = unique_candidates[index]
    
#Print results                        
print("Election Results")
print("----------------------")
print("Total Votes: ",votecount)
print("----------------------")
print(f"{unique_candidates[1]}: {round(percentage[1],3)}% ({votes[1]})")
print(f"{unique_candidates[2]}: {round(percentage[2],3)}% ({votes[2]})")
print(f"{unique_candidates[0]}: {round(percentage[0],3)}% ({votes[0]})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")