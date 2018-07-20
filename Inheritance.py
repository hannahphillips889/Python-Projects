class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self, text):
        self.type = text
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

class Square(Shape):
    def __init__(self, x):
        self.x = x
        self.y = x


s = Square(45)
print(s.area())


class Parent:
    def Show(self):
        print("Parent Method")

class Child(Parent):
    def Show(self):
        print("Child Method")

c = Child()
p = Parent()
p.Show()
c.Show()
