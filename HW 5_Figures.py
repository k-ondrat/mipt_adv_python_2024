import math

class Figure:
    def compute_surface(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def compute_circumference(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def __str__(self):
        return self.__class__.__name__

class Disc(Figure):
    def __init__(self, radius):
        self.radius = radius

    def compute_surface(self):
        return math.pi * self.radius**2

    def compute_circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"{super().__str__}(радиус={self.radius})"

class Polygon(Figure):
    def __init__(self, sides):
        self.sides = sides

    def compute_surface(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def compute_circumference(self):
        return sum(self.sides)

    def __str__(self):
        return f"{super().__str__}(стороны={self.sides})"

class RectangleFigure(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def compute_surface(self):
        return self.width * self.height

    def __str__(self):
        return f"{super().__str__}(ширина={self.width}, высота={self.height})"

class SquareFigure(RectangleFigure):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"{super().__str__}(сторона={self.width})"

class TriangleFigure(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.sides = [a, b, c]

    def compute_surface(self):
        p = self.compute_circumference() / 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))

    def __str__(self):
        return f"{super().__str__}(стороны={self.sides})"

class Rhombus(Figure):
    def __init__(self, diag1, diag2):
        self.diag1 = diag1
        self.diag2 = diag2

    def compute_surface(self):
        return (self.diag1 * self.diag2) / 2

    def compute_circumference(self):
        side = math.sqrt((self.diag1 / 2)**2 + (self.diag2 / 2)**2)
        return 4 * side

    def __str__(self):
        return f"{super().__str__}(диагональ1={self.diag1}, диагональ2={self.diag2})"


disc = Disc(5)
triangle = TriangleFigure(3, 4, 5)
rectangle = RectangleFigure(2, 3)
square = SquareFigure(4)
rhombus = Rhombus(5, 7)

print(disc)
print(triangle)
print(rectangle)
print(square)
print(rhombus)
