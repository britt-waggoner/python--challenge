import os
import csv

csvpath = os.path.join("election_data.csv")
out_file = os.path.join("txt_file.txt")

# Initialize a total vote counter.
total_votes = 0

# Variables
candidates = []
can_votes = {}
winner = ""
win_count = 0
win_percent = 0

# Winning Candidate and Winning Count Tracker


# Open and read csv file, header row
with open("election_data.csv") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # Print each row in the CSV file.
    for row in csvreader:
        
        # Total vote count
        total_votes += 1

        # Candidates
        can_name = row [2]

        # If no match, add to list and track votes
        if can_name not in candidates:

            candidates.append(can_name)
            can_votes[can_name] = 0

        can_votes[can_name] += 1 
      
    # Print election results
    results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    )
    print(results, end="")
     # Percentage and total # of votes per candidate
    for can_name in can_votes:
        
        votes = can_votes[can_name]
        vote_percent = float(votes)/float(total_votes)*100
        can_results = (f"{can_name}: {vote_percent:.1f}%  ({votes:,})\n")
        print(can_results)

        # Winner
        if (votes > win_count) and (vote_percent > win_percent):
            
            win_count = votes
            win_percent = vote_percent
            
            winner = can_name
    # Print final winner 
    final_winner =(
    f"Winner: {winner}\n"
    f"--------------------------\n"
    )
    print(final_winner, end="")

    # Save to text file.
    with open(out_file, "w") as outfile:
        outfile.write(results)
        outfile.write(can_results)
        outfile.write(final_winner)
