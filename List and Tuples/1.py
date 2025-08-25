# #Q 21 Find the sum of all elements in a list?

a = [1,2,3,4,5]
b=0
for c in a:
    b+=c
print(b)


# #Q 22 Find the maximum and minimum in a  list?

import math
h=[2,1,3,5,8,64,5]
maximum = max(h)
minimum = min(h)
print(maximum)
print(minimum)

# #Q 23 Reverse a list without using reverse method?
q=[6,5,6,7,8,9,43,1,4]
print(q[::-1])


# #Q 24 Find the second largest number in a list?

w = [1,3,6,4,9,7]
sorted_list = sorted(w, reverse=True)
second_largest = sorted_list[1]
print(second_largest)

# print("Second Largest:", second_largest)  # 7
    
# # Q 25 Remove duplicates from a list?

l = [6,7,8,9,6,7,8,9]
unique = list(set(l))
print(unique) 


# # Q 26 Merge two sorted lists into one sorted list?
q=[1,2,3,4,5,6]
w=[7,8,9]
s=q + w
s = sorted(s) 
print(s)

# # Q 27 Find common elements between two lists?
s=[1,7,4,5,6]
f=[4,3,2,1,6]
# Convert to set, then find intersection
z = set(s).intersection(set(f))
print(list(z))

# # Q 28 Count the frequency of elements ina list?

from collections import Counter

a = [1, 2, 2, 3, 4, 4, 4, 5]
freq = Counter(a)
print(freq)

# # Q 29 Convert a list into a tuple?
b=[2,5,8,1,4,7]
k=tuple(b)
print(k)

# #Q 30 Check if all elements in a list are unique?
t=[5,6,7,8,9,4,3,2,5,7]
t = [5, 6, 7, 8, 9, 4, 3, 2, 5, 7]

if len(t) == len(set(t)):
    print("All elements are unique")
else:
    print("Duplicates found")


