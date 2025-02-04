#stringPalindrome
string = "madam"
print(string == string[::-1])

#anagram checker
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen","silent"))

#word frequency
sentence = "the quick brown fox jumps over the lazy dog."
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word,0)+1
print(word_freq)

#extract digits and letters
mixed_string = "Python3.8 is awesome!"
digits = ''.join(filter(str.isdigit, mixed_string))
print(digits)

letters = ''.join(filter(str.isalpha, mixed_string))
print(letters)

#remove special characters
special = "Hello$$$ World!"
s = ''.join(filter(str.isalnum,special + " "))
print(s.strip())

'''output
True
True
{'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog.': 1}
38
Pythonisawesome
HelloWorld'''
