# Q 41 Generate a multiplication table of a given number?
a=2
for i in range(1,11):
    print(a , "X" , i  ,"=" , a*i)
    # print("\n")

# Q 42 Find factorial of a number?

h=5
a=1
for i in range(1,h+1):
    a*=i
print(a)

# Q 43 Generate Fibonacci series up to N terms?

n = 10   # number of terms
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b

# Q 44 Check if a number is prime?

num = 29

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")



# Q 45 Find all Prime numbers in a given range?

start = 10
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")


# Q 46 Calculate the sum of digits of a number?

num = 12345
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits:", sum_digits)

# Q 47 Reverse a number?

num = 12345
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)


# Q 48 Check if a number is an Armstrong number?

num = 153
temp = num
order = len(str(num))
sum_pow = 0

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** order
    temp //= 10

if sum_pow == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Q 49 Find the greatest common divisor (GCD) of two numbers?

import math
a = 36
b = 60
print("GCD:", math.gcd(a, b))

# Q 50 Find the least common multiple(LCM) of two numbers? 

import math
a = 36
b = 60
lcm = abs(a*b) // math.gcd(a, b)
print("LCM:", lcm)
