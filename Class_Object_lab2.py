#2. Distance Class (Overloading * Operator)
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __mul__(self, scalar):
        total_inches = (self.feet * 12 + self.inches) * scalar
        feet = total_inches // 12
        inches = total_inches % 12
        return Distance(feet, inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"


# Example Usage:
d1 = Distance(5, 8)
d2 = d1 * 3
print(d2)  # Output: 17 feet 0 inches
