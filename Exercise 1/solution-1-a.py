# improved solution for Question 1

c=0
l=[]

def FindMultipleFive(x,y):
    for i in range(x, y, 7):
        if i%5==0:
            return i

for i in range(2000, 3201):
    if i%7==0:
        a=i
        b=FindMultipleFive(i, 3201)
        break

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