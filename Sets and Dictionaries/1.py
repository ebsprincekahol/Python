# # Q 31 Find the union of two sets?

# a={1,2,3,4,5,4,3,2,1}
# b={9,8,7,6,5,4,6,8,9}
# c=a.union(b)
# print(c)

# # Q 32 Find the intersection of two sets?

# d={1,2,3,4,5,4,3,2,1}
# e={9,8,7,6,5,4,6,8,9}
# f=d.intersection(e)
# print(f)

# # Q 33 Find the difference between two sets?

# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}
# z = x.difference(y)   
# print(z)


# # Q 34 Check if a set is a subset of another?

a = {1, 5}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))

# # Q 35 Convert two lists into a dictionary?

# g = [3,4,5,4,3]
# h = [4,6,7,8,9]
# i = dict(zip(g, h))
# print(i)  

# # Q 36 Merge two dictionaries?

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = {**dict1, **dict2}
# print(merged)

# # Q 37 Get the key with the maximum value in dictionary?

# scores = {"a": 10, "b": 25, "c": 15}
# max_key = max(scores, key=scores.get)
# print(max_key)

# # Q 38 Count the frequency of words in a sentence using a dictionary?

# sentence = "python is easy and python is powerful"
# words = sentence.split()
# freq = {}
# for w in words:
#     freq[w] = freq.get(w, 0) + 1
# print(freq)

# # Q 39 Remove a key from a dictionary?

# data = {"a": 1, "b": 2, "c": 3}
# data.pop("b")
# print(data)

# # Q 40 Check if a key exists in a dictionary?

# info = {"name": "Prince", "age": 25}
# if "age" in info:
#     print("Key exists")
# else:
#     print("Key not found")




