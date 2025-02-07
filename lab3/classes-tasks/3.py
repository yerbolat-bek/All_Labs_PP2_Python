class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
