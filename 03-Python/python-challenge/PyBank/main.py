import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Resources", "output.txt")

date = []
pl = []
greatest_inc = 0
greatest_dec = 0
total = 0

with open(csvpath, newline="") as csvfile:
    with open(output_path, 'w', newline='') as textfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        for row in csvreader:
            date.append(row[0])
            pl.append(int(row[1]))

        for i in range(len(pl)):
            if int(pl[i]) - int(pl[i-1]) >= greatest_inc:
                greatest_inc = int(pl[i]) - int(pl[i-1])
                great_inc_month = date[i]
            elif int(pl[i]) - int(pl[i-1]) <= greatest_dec:
                greatest_dec = int(pl[i]) - int(pl[i-1])
                great_dec_month = date[i]

        total = sum(pl)
        
        average = round(total/len(date), 2)

        analysis=("Financial Analysis"
            "\n-----------------------------"
            f"\nTotal Month: {len(date)}"
            f"\nTotal: ${total}"
            f"\nAverage Change: ${average}"
            f"\nGreatest Increase in Profits: {great_inc_month} ({greatest_inc})"
            f"\nGreatest Decrease in Profits: {great_dec_month} ({greatest_dec})")
    
        textfile.write(str(analysis))

    print(analysis)