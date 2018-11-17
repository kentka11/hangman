# coding: UTF-8

#9-1
#with open("loop.py", "r") as f:
#    print(f.read())

#9-2
a = input("What is your favarite color?")
with open("answer.txt", "w", encoding="utf-8") as f:
    f.write(a)    
with open("answer.txt", "r") as f:
    print(f.read())

#9-3
import csv
lists = [["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]]

with open("theater.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for list1 in lists:
        w.writerow(list1)

with open("theater.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
