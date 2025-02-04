'''5.  Write a Python program that determines
the largest of three numbers entered by the user using nested if syntax.'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b:
    if a > 3:
        print(f'{a} is the largest number.')
    else :
        print(f'{c} is the largest number.')
else:
    if b > c:
        print(f'{b} is the largest number.')
    else :
        print(f'{c} is the largest number.')

'''output
Enter the first number: 10
Enter the second number: 20
Enter the third number: 30
30 is the largest number.'''
