#Longest Palindromic Substring
def longest_palindromic_substring(s):
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        temp = expand_center(i, i)
        if len(temp) > len(longest):
            longest = temp
        # Even-length palindrome
        temp = expand_center(i, i + 1)
        if len(temp) > len(longest):
            longest = temp
    return longest

print(longest_palindromic_substring("babad"))


#Character Frequency Analysis
def most_frequent_character(s):
    s = s.replace(" ", "").lower()
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max_char = max(frequency, key=frequency.get)
    return {'Character': max_char, 'Frequency': frequency[max_char]}

print(most_frequent_character("This is a test sentence"))


#String Compression
def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))  # Add last character and count

    return ''.join(compressed)

print(compress_string("aaabbccca"))


#Find Anagrams
def find_anagrams(word, lst):
    sorted_word = sorted(word)
    return [w for w in lst if sorted(w) == sorted_word]

print(find_anagrams('listen', ['enlist', 'google', 'inlets', 'banana']))


#Caesar Cipher Decoder
def caesar_cipher_decoder(cipher, shift):
    decoded = []
    for char in cipher:
        if char.isalpha():
            new_char = chr((ord(char) - shift - 97) % 26 + 97)
            decoded.append(new_char)
        else:
            decoded.append(char)
    return ''.join(decoded)

print(caesar_cipher_decoder('dwwdfn', 3))



