import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Resources", "output.txt")

date = []
pl = []

with open(csvpath, newline="") as csvfile:
    with open(output_path, 'w', newline='') as textfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        for row in csvreader:
            date.append(row[0])
            pl.append(int(row[1]))

        totalmonth=len(date)
        total=sum(pl)
        average=round(total/totalmonth, 2)
        increase=max(pl)
        increasedate=date[pl.index(increase)]
        decrease=min(pl)
        decreasedate=date[pl.index(decrease)]

        analysis=("Financial Analysis"
            "\n-----------------------------"
            f"\nTotal Month: {totalmonth}"
            f"\nTotal: ${total}"
            f"\nAverage Change: ${average}"
            f"\nGreatest Increase in Profits: {increasedate} ({increase})"
            f"\nGreatest Decrease in Profits: {decreasedate} ({decrease})")
    
        textfile.write(str(analysis))

    print(analysis)