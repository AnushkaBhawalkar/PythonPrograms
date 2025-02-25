#1. Time Class (Overloading + Operator)
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        minutes = total_minutes % 60
        hours = self.hours + other.hours + extra_hours
        return Time(hours, minutes)

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"


# Example Usage:
t1 = Time(2, 50)
t2 = Time(1, 30)
t3 = t1 + t2
print(t3)  # Output: 4 hours 20 minutes


