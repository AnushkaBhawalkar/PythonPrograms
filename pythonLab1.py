"""Q.1 Write a program to accept a number and display its square and cube.
Q.2 Write a program to accept 5 float values and display its sum and average.
Q.3 Write a program to calculate the area of rectangle."""

#1stprogram
num = int(input("Enter a number: "))
Square = num ** 2
Cube = num ** 3
print(f"The square of {num} is {Square}.")
print(f"The cube of {num} is {Cube}.")

#output
Enter a number: 3
The square of 3 is 9.
The cube of 3 is 27.

#2ndprogram
values = [float(input("Enter a number: "))for _ in range(5)]
Total_sum = sum(values)
Average = Total_sum / 5
print("Sum: ", Total_sum)
print("Average: ", Average)

#output
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
Sum:  15.0
Average:  3.0

#3rdprogram
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

#output
Enter the length of the rectangle: 10
Enter the width of the rectangle: 30
The area of the rectangle is: 300.0

