import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Resources", "output.txt")

total = 0
poll = {}
candidates = []
num_votes = []

with open(csvpath, newline="") as csvfile:
    with open(output_path, 'w', newline='') as textfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        for row in csvreader:
        
            total += 1

            if row[2] in poll.keys():
                poll[row[2]] = poll[row[2]] + 1
            else:
                poll[row[2]] = 1
        

        for key, value in poll.items():
            candidates.append(key)
            num_votes.append(value)

        candidate1 = "{:.2%}".format(num_votes[0]/total)
        candidate2 = "{:.2%}".format(num_votes[1]/total)
        candidate3 = "{:.2%}".format(num_votes[2]/total)
        candidate4 = "{:.2%}".format(num_votes[3]/total)
        winner=candidates[num_votes.index(max(num_votes))]

        results=("Election Results"
            "\n------------------------"
            f"\nTotal Votes: {total}"
            "\n------------------------"
            f"\n{candidates[0]}: {candidate1} ({num_votes[0]})"
            f"\n{candidates[1]}: {candidate2} ({num_votes[1]})"
            f"\n{candidates[2]}: {candidate3} ({num_votes[2]})"
            f"\n{candidates[3]}: {candidate4} ({num_votes[3]})"
            "\n------------------------"
            f"\nWinner: {winner}"
            "\n------------------------")
        
        textfile.write(str(results))

    print(results)