Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cubes = {num:num**3 for num in range(1,6)}
cubes
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
student={'name':'John','age':22,'grade':'A'}
student['name']
'John'
student['grade']='A+'
student
{'name': 'John', 'age': 22, 'grade': 'A+'}
inventory={'apples':10,'bananas':5}
inventory['oranges']=7
inventory
{'apples': 10, 'bananas': 5, 'oranges': 7}
inventory.pop('bananas')
5
inventory
{'apples': 10, 'oranges': 7}
scores={'Alice':85,'Bob':90,'Charlie':88}
scores
{'Alice': 85, 'Bob': 90, 'Charlie': 88}
'David' in scores
False
sample_dict={'a':1,'b':2,'c':3}
sample_dict.items
<built-in method items of dict object at 0x000001DE70737CC0>
sample_dict.items()
dict_items([('a', 1), ('b', 2), ('c', 3)])
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
dict1+dict2
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict1+dict2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
merged_dict=dict1.copy()
merged_dict.update(dict2)
merged_dict
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1|dict2
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
squares={num:num**2 for num in range(1,11)}
squares
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>>> even_suares={num:num**@ for num in range(1,11) if num%2 == 0}
SyntaxError: invalid syntax
>>> even_suares={num:num**2 for num in range(1,11) if num%2 == 0}
>>> even_squares
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    even_squares
NameError: name 'even_squares' is not defined. Did you mean: 'even_suares'?
>>> even_suares
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
>>> original_dict={'a':1,'b':2,'c':3}
>>> reversed_dict={value: key for key, value in original_dict.items()}
>>> reversed_dict
{1: 'a', 2: 'b', 3: 'c'}
>>> string="Programming"
>>> char_frequency={char:string.count(char) for char in set(string)}
>>> char_frequency
{'g': 2, 'r': 2, 'P': 1, 'a': 1, 'n': 1, 'm': 2, 'o': 1, 'i': 1}
>>> nested_dict={i{j:i*j for j in range(1,4)} for i in range(1,4)}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> nested_dict={i:{j:i*j for j in range(1,4)} for i in range(1,4)}
>>> nested_dict
{1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
>>> keys=['name','age','city']
>>> values=['Alice',22,'New Jersey']
>>> dictionary={keys[i]:values[i] for i in range(len(keys))}
>>> dictionary
{'name': 'Alice', 'age': 22, 'city': 'New Jersey'}
>>> marks = {'Alice': 55, 'Bob': 65, 'Charlie': 80, 'David': 72}
>>> marks1={key: value for key, value in marks.items() if value > 80}
>>> marks1
{}
>>> table={i: 5 * i for i in range(1, 11)}
>>> table
{1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}
>>> data = [('a',10),('b',20),('c',30)]
>>> converted_dict={key:value for key, value in data}
>>> converted_dict
{'a': 10, 'b': 20, 'c': 30}
