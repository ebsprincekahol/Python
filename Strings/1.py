# Q11 Reverse a String ?
# Format: s[start:stop:step]
# If step = -1, it walks from end to start.
# Leaving start and stop empty means “use full string”.
s = "Hello"
# Step 1: Use slicing with negative step
rev1 = s[::-1]          # 'olleH'
# (Optional) Step 2: Other ways (for learning)
rev2 = "".join(reversed(s))  # also 'olleH'
print(rev1)



#Q12 Count vowels and consonants in a string.
b = "akjfeiknghodrfu"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in b:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

#Q13 Check if a string is a palindrome.
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    

#Q14 Find the frequency of each character in a string.
s = "hello world"
freq = {}

for ch in s:
    # Step 1: increase count if exists, else start at 1
    freq[ch] = freq.get(ch, 0) + 1

print(freq)   # e.g., {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Q15 Remove all space sfrom a string?

c = "  hello welcome  "
print(c.strip())      # 'hello welcome'
print(c.replace(" ", ""))   # 'hellowelcome'

# Q16 Replace all vowels in a string with *?

text = "Hello World"
vowels = "aeiouAEIOU"   # vowels list
result = ""

for char in text:       # har character check karenge
    if char in vowels:  
        result += "*"   # vowel mila → replace with *
    else:
        result += char  # normal char → same rakho

print(result)   # H*ll* W*rld
# Step by step run:
# H → not vowel → add H
# e → vowel → add *
# l → not vowel → add l
# l → not vowel → add l
# o → vowel → add *
# and so on...



#Q17 Check if two strings are anagrams?

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):   # dono ko sort karke compare karo
    print("Anagram")
else:
    print("Not anagram")
# Step by step run:
# listen → sort → eilnst
# silent → sort → eilnst
# Same hai → Anagram



#Q18 Convert a string to uppercase without using .upper()?

text = "hello welcome"
result = ""

for char in text:
    if 'a' <= char <= 'z':   # check lowercase
        result += chr(ord(char) - 32)   # convert to uppercase
    else:
        result += char        # keep spaces or symbols same

print(result)


# Step 1: Initial values
# text = "hello welcome"
# result = "" (empty string where we will store the output)

# Step 2: Loop through each character
# The loop goes one by one through each character in text.
# So order will be:
# 'h' → 'e' → 'l' → 'l' → 'o' → ' ' (space) → 'w' → 'e' → 'l' → 'c' → 'o' → 'm' → 'e'

# Step 3: Check if character is lowercase
# if 'a' <= char <= 'z':
#  This checks: is the character between 'a' and 'z' in ASCII table?
# If yes → character is lowercase.
# If no → it is space, symbol, or already uppercase.

# Step 4: Convert lowercase → uppercase
# result += chr(ord(char) - 32)
# ord(char) → gives ASCII number.
# Example: ord('h') = 104
# ord(char) - 32 → subtracts 32.
# Example: 104 - 32 = 72
# chr(72) → converts back number → letter.
# chr(72) = 'H'
# So lowercase 'h' becomes uppercase 'H'.

# Step 5: If not lowercase
# else:
#     result += char
# If the character is not lowercase (like ' ' space), it is added without change.

# Step 6: Final Output
# "hello welcome" → "HELLO WELCOME"


#Q19 Find the longest word in a senetence?

sentence = "Python is a powerful programming language"
words = sentence.split()          # ['Python','is','a','powerful','programming','language']

longest = max(words, key=len)     # sabse lamba word

print("Longest word:", longest)   # programming

#Q20 Count the number of words in a string?

text = "Hello welcome to Python"
words = text.split()          # ['Hello','welcome','to','Python']
print("Word count:", len(words))   # 4

