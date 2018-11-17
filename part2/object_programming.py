#coding: UTF-8

class Shape:
  def what_am_i(self):
    return "I am a shape"


class Rectangle(Shape):
  def __init__(self, w, l):
    self.width = w
    self.len = l

  def calculate_perimeter(self):
    return ( self.width + self.len ) * 2

class Square(Shape):
  def __init__(self, w, l):
    self.width = w
    self.len = l

  def calculate_perimeter(self):
    return ( self.width + self.len ) * 2

  def change_size(self, w, l):
    self.width += w
    self.len += l

a_rectangle = Rectangle(7, 9)
print(a_rectangle.calculate_perimeter())
print(a_rectangle.what_am_i())

a_square = Square(5, 7)
print(a_square.calculate_perimeter())
print("width:" + str(a_square.width))
print("length:" + str(a_square.len))

a_square.change_size(8, 9)
print(a_square.calculate_perimeter())
print("width:" + str(a_square.width))
print("length:" + str(a_square.len))
print(a_square.what_am_i())

class Horse:
  def __init__(self, name, rider):
    self.name = name
    self.rider = rider

class Rider:
  def __init__(self, name):
    self.name = name

nick = Rider("nick")
black = Horse("black", nick)
print(black.rider)


