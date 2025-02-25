#3. Rectangle Class (Overloading == Operator)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.area() == other.area()

    def __str__(self):
        return f"Rectangle({self.length} x {self.width})"


# Example Usage:
r1 = Rectangle(4, 5)
r2 = Rectangle(2, 10)
r3 = Rectangle(3, 6)

print(r1 == r2)  # Output: True (both have area 20)
print(r1 == r3)  # Output: False (20 != 18)
