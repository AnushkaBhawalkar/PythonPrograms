Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Python Programming"
text[0]
'P'
text[-1]
'g'
text[6]
' '
text[0:6]
'Python'
text[7:]
'Programming'
text[::2]
'Pto rgamn'
text[::-1]
'gnimmargorP nohtyP'
nested_text="Learn Python [Basics]"
nested_text[14:20]
'Basics'
nested_text[13:21]
'[Basics]'

sentence="Data Analytics using Python"
len(sentence)
27
s = "hello world"
s.upper()
'HELLO WORLD'
s1="PYTHON IS FUN"
s1.lower()
'python is fun'
s2."machine learning"
SyntaxError: invalid syntax
s2="machine learning"
s2.capitalize()
'Machine learning'

quote = "The quick brown fox jumps over the lazy dog"
quote.find("fox")
16
quote.replace("lazy dog", "active dog")
'The quick brown fox jumps over the active dog'

words = "apple,banana,cherry"
word_list=words.split(",")
word_list
['apple', 'banana', 'cherry']
print(" ".join(word_list))
apple banana cherry

string = "Learn Python Programming"
print("Python" in string)
True
string.startswith("Learn")
True
string.endswith("Programming")
True

messy_text=" Clean this text "
messy_text.lstrip()
'Clean this text '
messy_text.rstrip()
' Clean this text'
messy_text.strip()
'Clean this text'

paragraph = "Python is powerful. Python is versatile. Python is easy to learn."
paragraph.count("Python")
3
paragraph.count("i")
4
