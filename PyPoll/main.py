#This script will count votes cast for each candidate and identify the winner of the election

# set modules
import os
import csv

#Create the variables needed for exercise
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentage = {}
winner_votes = 0
winner = ""

# Open csv file to be used to count the votes
csvpath = os.path.join("Resources/election_data.csv")

#Open csv reader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    #print(csvreader)


    # Counting the votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
    else:
         candidate_votes[candidate] = 1

    # Calculate the voter percentages and name the winner
    for person, vote_count in candidate_votes.items():
        candidate_percentage[person] = '{0:.0%}'.format(vote_count / total_votes)
        if vote_count > winner_votes:
            winner_votes = vote_count
            winner = person  

   # Print out the results 
    print(f"Election Results")
    print(f"-" * 25)
    print(f"Total Votes: {total_votes}")
    print(f"-" * 25)
    for person, vote_count in candidate_votes.items():
        print(f"{person}: {candidate_percentage[person]} ({vote_count})")
    print(f"-" * 25)
    print(f"Winner: {winner}")
    print(f"-" * 25)



    