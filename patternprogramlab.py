'''1.
1
2 3
4 5 6
7 8 9 10

n = 4
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    print()

2.
5 4 3 2 1
  4 3 2 1
    3 2 1
      2 1
        1
n = 5
for i in range(n):
    print(" " * (2 * i), end="")
    for j in range(n-i, 0, -1):
        print(j, end=" ")
    print()

3.
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

4.
A
A B C
A B C D
A B C D E
A B C D E F

n = 6
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end = " ")
    print()


5.
  *
    *
   ***
  ***
 ***'''

n = 5
for i in range(1, n + 1):
    if i % 2 == 1:
        print(" " * (n - i) + "*" * i)
    else:
        print(" " * (n - i) + "*" * i)
