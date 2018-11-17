#coding: UTF-8

# カプセル化
class Rectangle:
  def __init__(self, w, h):
    self.weight = w 
    self.height = h

  def area(self):
    return self.weight * self.height / 2

my_rectangle = Rectangle(5, 9)
print(my_rectangle.area())

# 抽象化
# 継承

class Shape(Rectangle):
  pass

a_rectangle = Shape(9, 3)
print(a_rectangle.area())


