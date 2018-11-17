# coding: UTF-8

#7-1
lists = ["Waking Dead", "Antradu", "Vampire Diaries", "The Soprano"]
for str1 in lists:
    print(str1)

#7-2
#for i in range(25, 51):
#    print(i)

#7-3
i = 0
for str1 in lists:
    print("index :" + str(i) + " " + str1)
    i += 1

#7-4
qs = ["How old is Manami?",
      "How much is the glass?",
      "How many people are in the building?"]

n = 0
while True:
    print("Type number or q to quit")
    a = input(qs[n])
    if a == "q":
        break
    elif a == "2" and n == 0:
        print("Q1:Correct")
    elif a != "2" and n == 0:
        print("Q1:Incorrect")
    elif a == "100" and n == 1:
        print("Q2:Correct")
    elif a != "100" and n == 1:
        print("Q2:Incorrect")
    elif a == "10000" and n == 2:
        print("Q3:Correct")
    elif a != "10000" and n == 2:
        print("Q3:Incorrect")
    
    n = (n + 1) % 3


#7-5
lists1 = [8,19,148,4]
lists2 = [9,1,33,83]
new_lists = []
for num1 in lists1:
    for num2 in lists2:
        new_lists.append(num1*num2)
print(new_lists)

