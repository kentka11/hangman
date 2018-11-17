
# coding: UTF-8

#6-1
str1 = "Kamyu"
print(str1)
for i in range(len(str1)):
    print(str1[i])

#6-2
#print("I wrote [input1] and sent it to [input2] yesterday.")

#input1 = input("please input for input1")
#input2 = input("please input for input2")

#print("I wrote " + input1 + " and sent it to " + input2 + " yesterday.")

#6-3
str2 = "aldous Huxley was born in 1894."
print(str2.capitalize())

#6-4
str3 = "Where? Who? When?"
lists = str3.split(" ")
print(lists)

#6-5
lists =["The", "fox", "jumped", "over", "the", "fence", "."]
space = " "
no_space = ""
str4 = ""
print(space.join(lists))
#for i in range(len(lists)):
#    if i == len(lists) - 1:
#        print(lists[i])
#        str4 = str4 + no_space.join(lists[i])
#    else:
#        print(lists[i])
#        str4 = str4 + space.join(lists[i])
        

#6-6
str5 = "A screaming comes across the sky."
print(str5.replace("s", "$"))

#6-7
str6 = "Hemingway"
print(str6.index("m"))

#6-8
str7 = '"Life is beatiful"'
print(str7)

#6-9
str8 = "three" + " three " + "three"
print(str8)
print(("three "*3).strip())

#6-10
str9 = "It's in April, and it is cold."
print(str9[:str9.index(",")])
