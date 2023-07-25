# improved solution for Question 1

c=0
l=[]

def FindMultiple(x,y,z,q):
    for i in range(x, y, z):
        if i%q==0:
            return i

a = FindMultiple(2000, 3201, 1, 7)

b = FindMultiple(a, 3201, 7, 5)

while a<b:
    l.append(str(a))
    a += 7
    
while a<=3200:
    if c==0:
        c=4
        a += 7
    else:
        l.append(str(a))
        a += 7
        c -= 1
        
print(','.join(l))  