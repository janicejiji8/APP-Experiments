class Shape:
    """Base class representing a generic shape."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """To be overridden by subclasses."""
        return 0

    def describe(self):
        return f"{self.name} has an area of {self.area():.2f}"


class Rectangle(Shape):
    """Rectangle inherits from Shape."""

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    """Circle inherits from Shape."""

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    """Triangle inherits from Shape."""

    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def main():
    shapes = [
        Rectangle(width=5, height=3),
        Circle(radius=4),
        Triangle(base=6, height=2),
    ]

    # Polymorphism
    for shape in shapes:
        print(shape.describe())


if __name__ == "__main__":
    main()
