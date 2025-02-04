#Program to check whether the given number is palindrome or not using while loop.

num = int(input("Enter a number to check if it is a palindrome: "))
temp = num
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if temp == reverse:
    print(f"{temp} is a palindrome")
else:
    print(f"{temp} is not palindrome")

output
Enter a number to check if it is a palindrome: 1234321
1234321 is a palindrome

#Program to find the sum of digits of a given number using while loop.

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(f'The sum of digits is {sum}!')

ouput
Enter a number: 280503
The sum of digits is 18!





