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
        
rectangle = Shape(100, 45)
print(rectangle.area())


class Area:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

rectangle = Area(3, 6)
print(rectangle.area())
