# Q21 Find the sum of all elements in a list?

a=[1,2,3,4,5]
b=0
for i in a:
    b+=i
print(b)

# Q22 Find the maximum and minimum in a list?
import math
c=[1,2,3,4,5,6,7]
d=[3,4,5,6,7,7,8]
e=max(c)
f=min(d)
print(e)
print(f)

# Q23 Reverse a list without using reverse method? 

y=[3,5,6,7,8]
print(y[::-1])

# Q24 find the second largest muber in a list?

r=[3,4,5,6,2,1]
t=sorted(r,reverse=True)
r=t[1]
print(r)

# Q25 Remove duplicates from a list?

w=[3,5,6,7,8,9,4,3,2,1]
g=set(w)
h=list(g)
print(h)

# Q26 Merge two sorted lists into one sorted list?

d=[4,5,6,7]
j=[1,2,3,4]
v=sorted(d+j)
print(v)

# Q27 Find common elements between two lists?

q=[3,4,3,4]
za=[4,3,2,1]
s=set(q).intersection(za)
print(s)   # {3,4}


# Q28 Count the frequency of elements in a list?


nums=[1,2,2,3,3,3,4]
freq={}
for n in nums:
    freq[n]=freq.get(n,0)+1
print(freq)   # {1:1, 2:2, 3:3, 4:1}

# Q29 Convert a list into a tuple?

x=[1,2,3,2,1]
l=tuple(x)
print(l)

# Q30 Check if all elementsin a list are unique?

nums=[1,2,3,4,5]
if len(nums)==len(set(nums)):
    print("All elements are unique")
else:
    print("Not unique")


