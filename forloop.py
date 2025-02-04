#Program to display the multiplication table of a given number.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f'{i} x {num} = {num*i}')

ouptput
Enter a number: 15
1 x 15 = 15
2 x 15 = 30
3 x 15 = 45
4 x 15 = 60
5 x 15 = 75
6 x 15 = 90
7 x 15 = 105
8 x 15 = 120
9 x 15 = 135
10 x 15 = 150


#Program to disply the factorial of a number.
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i

#print(f'Factorial of {num} is {factorial}')

output
Enter a number: 5
Factorial of 5 is 120


#Program to check whether the given number is prime or not
num = int(input("Enter a number: "))
print(f'The prime numbers from 1 to {num} are: ')
for i in range(1, num+1, 2):
    print(i)

output
Enter a number: 10
The prime numbers from 1 to 10 are: 
1
3
5
7
9


#Program to print numbers from N to 1.
num = int(input("Enter a number: "))
for i in range(num, 0, -1):
    print(i , end=" ")

output
Enter a number: 10
10 9 8 7 6 5 4 3 2 1
