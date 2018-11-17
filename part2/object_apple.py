import math

class Apple:
  def __init__(self, w, s, c, sg):
    self.weight = w
    self.size = s
    self.color = c
    self.suger = sg
    print("Created!!")

my_apple = Apple(10, 1999, "yellow", 1029)
print(my_apple.weight)
print(my_apple.size)
print(my_apple.color)
print(my_apple.suger)


class Circle:
  def __init__(self, r):
    self.r = r

  def area(self):
    return self.r**2*math.pi

my_circle = Circle(5)
print(my_circle.area())

class Triangle:
  def __init__(self, w, h):
    self.weight = w
    self.height = h

  def area(self):
    return self.height * self.weight / 2

my_triangle = Triangle(5, 9)
print(my_triangle.area())

class Hexagon:
  def __init__(self, s):
    self.sideLength = s
  
  def calculate_perimeter(self):
    return 3 * math.sqrt(3) * self.sideLength

my_hexagon = Hexagon(9)
print(my_hexagon.calculate_perimeter())

