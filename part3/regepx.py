#coding: UTF-8

import re

#l = "Beautiful"
#l = "beautiful"
#l = "^[iI]f"
#l = "th[oa]"
l = "\d"
matches = []

#with open("zen.txt", "r") as f:
#  for line in f.readlines():
#    #matches = re.findall(l, line)
#    matches = re.findall(l, line, re.IGNORECASE)
#    print(matches)

with open("zen.txt", "r") as f:
  m = re.findall(l, f.read(), re.MULTILINE)
print(m)

