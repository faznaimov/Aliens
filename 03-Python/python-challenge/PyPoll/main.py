import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Resources", "output.txt")

voter_id = []
county = []
candidate = []

with open(csvpath, newline="") as csvfile:
    with open(output_path, 'w', newline='') as textfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        for row in csvreader:
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        
        total = len(voter_id)
        candidates_unique = set(candidate)
        winner = 
        vote_number = 
        vote_percentage = 
        

        results=("Election Results"
            "\n-------------------------"
            f"\nTotal Votes: {total}"
            "\n-------------------------"
            f"\nKhan: ${total}"
            f"\nCorrey: ${average}"
            f"\nLi: {increasedate}"
            f"\nO'Tooley: {decreasedate}"
            "\n-------------------------"
            f"Winner: {winner}"
            "\n-------------------------")
    
        textfile.write(str(results))

    print(results)