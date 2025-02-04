Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits={'Apple','Banana','Cherry'}
>>> print("'apple' is in the set: ",'Apple' im fruits)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("'apple' is in the set: ",'Apple' in fruits)
'apple' is in the set:  True
>>> numbers={10,20,30,40,50}
>>> len(numbers)
5
>>> duplicates=[1,2,2,3,4,4,5]
>>> list(set(duplicates))
[1, 2, 3, 4, 5]
>>> list1=[1,2,3,4]
>>> list2=[3,4,5,6]
>>> common=set(list1).intersection(set(list2))
>>> common
{3, 4}
>>> string="programming"
>>> unique_char=set(string)
>>> unique_char
{'n', 'm', 'a', 'o', 'g', 'i', 'p', 'r'}
>>> set1={1,2,3}
>>> set2={3,4,5}
>>> set1.union(set2)
{1, 2, 3, 4, 5}
>>> A={'a','b','c'}
>>> B={'b','c','d'}
>>> A.intersection(B)
{'b', 'c'}
>>> X={1,2,3,4}
>>> Y={3,4,5,6}
>>> X.difference(Y)
{1, 2}
