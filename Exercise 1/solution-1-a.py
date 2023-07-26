# improved solution for Question 1

l=[]

lowerRange,upperRange = (int(x) for x in input("Enter two values for range ").split(","))
d = int(input("Enter one value to find all multiples of in the given range "))
e = int(input("Enter one value to exclude all multiples of in the given range "))

# x: Lower Range for loop, y: Upper Range for loop, z: Increment value, q: Value to check for multiple
def FindMultiple(x,y,z,q):
    for i in range(x, y, z):
        if i%q==0:
            return i

a = FindMultiple(lowerRange, upperRange, 1, d)

b = FindMultiple(a, upperRange, d, e)

c = int((b-a)/d)
    
while a<=upperRange:
    if c<=0:
        c=(e-1)
        a += d
    else:
        l.append(str(a))
        a += d
        c -= 1
        
print(','.join(l))
