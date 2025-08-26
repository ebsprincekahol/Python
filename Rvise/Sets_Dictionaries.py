# Q 31 Find the union of two sets?

a={1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1}
b={0,5,4,3,6,5,2,5}
c=a.union(b)
print(c)

# Q 32 Find the intersection of two sets?

d={0,4,8,3,6,9}
e={4,5,6,7,8,9}
f=d.intersection(e)
print(f)

# Q 33 Find the difference between two sets?

g={1,8,9,5,6}
h={9,5,4,6,2}
i=g.difference(h)
print(i)

# Q 34 Check if a set is a subset of another?

j={4,5,6,7}
k={2,3,4,5,6,7}
print(j.issubset(k)) 

# Q 35 Convert two lists into a dictionary?

m=[1,2,3,4,5]
n=[6,7,8,9,10,11]
o=dict(zip(m,n))
print(o)

# Q 36 Merge two dictionaries?

p={"a":1,"b":2,"c":3}
q={"h":7,"u":1}
r=dict(**p,**q)
print(r)
l={**p,**q}
print(l)

# Q 37 Get the key with the maximum value in dictionary?

s={"a":1,"b":2,"c":7,"r":6}
t=max(s, key=s.get)
print(t)

# Q 38 Count the frequency of words in a sentence using a dictionary?

# Q 39 Remove a key from a dictionary?

u={"w":1,"z":2,"v":5}
z=u.pop("w")
print(u)

# Q 40 Check if a key exists in a dictionary?

d={"t":4,"y":7}
if "t" in d:
    print("yes")
else:
    print("no")







