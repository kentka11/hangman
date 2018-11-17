# coding: UTF-8

#st = open("st.txt", "w")
st = open("st.txt", "w", encoding="utf-8")
print(st)
st.write("hello python world!")
st.close()

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

my_list = []
with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read())
    my_list.append(f.read())

with open("st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())
    print(f.read())
print(my_list)

import csv

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
