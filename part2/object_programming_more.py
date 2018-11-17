#coding: UTF-8

class Shape:
  def what_am_i(self):
    print("I am a shape!")

class Square:
  #クラス変数
  square_list = []
  def __init__(self, l):
    self.len = l
    self.square_list.append(self)

  def calculate_perimeter(self):
    return self.len * 4

  def __repr__(self):
    return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)

lists = []  
for i in range(1, 10):
  lists.append(Square(i))

for i in lists:
  print(i.square_list)
  print(i.len)
  print(i.calculate_perimeter())
  print(i)

