# Improved solution for Question 2

# This allows for more than one number to be computed at once

a=[]

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

n=int(input('Number of elements to find their factorial:'))

for i in range (0, n):
    x=int(input())
    a.append(x)
    
b = list(map(factorial, a))

print(','.join(b))