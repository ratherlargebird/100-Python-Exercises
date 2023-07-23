# improved solution for Question 1

a=0
b=0
c=0
l=[]

# find the first number that is divisible by 7
for x in range(2000, 3201):
    if x%7==0:
        a=x
        break
        
# Find the first number divisble by 5

for y in range(a, 3201):
    if y%5==0:
        b=y
        break

# Add numbers that are divisible by 7 to the list but skip every 5th term after first term divisible by 5
        
while a<3200:
    if a<b:
        l.append(str(a))
        a += 7
    else:
        c += 1
        if c != 4:
            l.append(str(a))
            a += 7
        else:
            c = 0
            a += 7
        
print(','.join(l))  