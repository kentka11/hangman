
# class Square:
#  pass

# print(Square)

class Rectangle:
  def __init__(self, w, l):
    self.width = w
    self.len = l

  def print_size(self):
    print("{} by {}".format(self.width, self.len))


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

class Orange:
  def __init__(self, w, c):
    self.weight = w
    self.color = c
    self.mold = 0
    print("Created!!")

  def rot(self, days, temp):
    """temp(温度)は摂氏"""
    self.mold = days * temp

orl = Orange(10, "dark orange")
print(orl.weight)
print(orl.color)
orl.weight = 1000000
print(orl.weight)

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)
