#coding: UTF-8

import re

l = "Dutch"
str1 = "479, 501, 870. California 209, 213, 650."
find = "\d+"

str2 = "The ghost that says boo haunts the loo"
fnd2 = ".oo"

with open("zen.txt", "r") as f:
  matches = re.findall(l, f.read(), re.MULTILINE)
print(matches)

found = re.findall(find, str1)
print(found)

found = re.findall(fnd2, str2)
print(found)

