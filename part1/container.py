#1 favrite musician list

import datetime

#2 list
musicians = ["Micheal Jackson", "Queen", "Beatles", "Mr.Children", "Radwinps"]
print(musicians)
musicians.append("Yuzu")
print(musicians)
print(len(musicians))

#3 tuple
tuple_list = ("Queen", 1945, 0.18672, "2018/08/19", datetime.date.today())
print(tuple_list)
print(tuple_list[1])

#4 dictionary
dict = {"1": "Queen",
        "2": "Micheal Jackson",
        "3": "Beatles",
        "4": "Mr.Children",
        "5": "RADWINPS"
        }

for i in range(5):
    if str(i) in dict:
        print(dict[str(i)])

#5 
musician_dict = {"Queen": "We are the chanpion",
        "Micheal Jackson": "We are the world",
        "Beatles": "Yesterday",
        "Mr.Children": "Inocent World",
        "RADWINPS": "September"
        }
print(musician_dict)

#6 set container
s = set(musician_dict)
print(s)
print(len(s))
s.add("Carpentars")
print(len(s))
