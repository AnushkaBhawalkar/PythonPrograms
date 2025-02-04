#Simple Comprehension

'''n = [3,4,5,6,7]
squares=[x**2 for x in n]
print(squares)'''


#With Condition filters even numbers

'''even_num=[x for x in range(20) if x%2==0]
print(even_num)'''


#Nested Loops

'''co_ordinates= [(x,y) for x in range(5) for y in range(3)]
print(co_ordinates)'''


#With if else condition

'''result=["Even" if num%2==0 else "Odd" for num in range(10)]
print(result)'''


#Filter Divisible numbers

'''numbers=[x for x in range(1,51) if x%5==0]
print(numbers)'''


#Extract vowels from the string

'''string="Comprehension"
vowels=[ch for ch in string if ch in 'aeiou']
print(vowels)'''


#Generate prime numbers

'''primes=[x for x in range(2,50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
print(primes)'''


#Factorial

import math
numbers=[1,2,3,4,5]
factorials=[math.factorial(num) for num in numbers]
print (factorials)
