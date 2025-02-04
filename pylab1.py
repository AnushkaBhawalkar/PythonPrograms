"""1. Write a Python program that takes a number as input and prints "Even"
if the number is even and "Odd" if it's odd."""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f'{num} is even.')
else:
    print(f'{num} is odd')

'''output
Enter a number: 23
23 is odd''' 
