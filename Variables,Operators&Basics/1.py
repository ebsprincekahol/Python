# Q1 Print your names and age?
name = "Prince"
age = 27
print(f"My name is {name} and age is {age}")
# Alternative:
print("My name is", name, "and age is", age)

# Q2 Swap your numbers without using a third variable?
a=10
b=20
b=b-a
a=a+b
print("A :",a)
print("B :",b)
# But in Python we can do it in one line:
a, b = b, a

# Q3 Find the square and cube of a number?
a = 4
print("Square:", a**2)   
print("Cube:", a**3) 

# Q4 Convert Celsius to Fahrenheit?
# Formula F=9/5*c+32

celsius = 37
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)


# Q5 Calculate the area of a circle?
# Formula=Area=π×r2

import math
radius = 7
area = math.pi * (radius ** 2)
print(math.pi)
print("Area of Circle:", area)

# Q6 Find the largest of three numbers?
numbers = [3, 2, 1]
result = max(numbers)
print("Largest number is:", result)

# Or without using max():

a, b, c = 3, 2, 1
if a >= b and a >= c:
    result = a
elif b >= a and b >= c:
    result = b
else:
    result = c
print("Largest number is:", result)

#Q7 Check if a number is even or odd?
number1=9
if(number1%2==0):
    print(number1,"is even number")
else:
    print(number1,"is oddd number")

# Q8 Calculate the simple interest
# The formula for simple interest is: SI = (P × R × T) / 100, where P is the principal, R is the rate, and T is the time.
p=100
R=50
T=80
SI=(p*R*T)/100
print(SI)

# Q9Check if a number is positive ,negative ,or zero
num = -5
if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print("Number is Zero")


#Q10Find the remainder whne a number is divided by another number
a = 17
b = 5
remainder = a % b
print("Remainder when", a, "is divided by", b, ":", remainder)



