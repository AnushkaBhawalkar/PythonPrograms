'''6. write a program to accept an operator symbol(+,-,*,/,%)
and two numbers and perform the arithmetic operations.'''

operator = input("Enter an operator (+, -, /, *, %): ")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if operator == "+":
    print(f'The result is {a + b}')
elif operator == "-":
    print(f'The result is {a - b}')
elif operator == "/":
    if b != 0:
        print(f'The result is {a / b}')
    else:
        print("Error")
elif operator == "*":
    print(f'The result is {a * b}')
elif operator == "%":
    if b != 0:
        print(f'The result is {a - b}')
    else:
        pritn("Error")
else:
    print("Invalid operator")

'''output
Enter an operator (+, -, /, *, %): %
Enter the first number: 45
Enter the second number: 5
The result is 40'''
