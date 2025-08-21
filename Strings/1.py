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

