# improved solution for Question 1

a=0
b=0
l=[]

# find the first number that is divisible by 7
for x in range(2000, 3201):
    if x%7==0:
        a=x
        break

# add all numbers divisible by 7 to a list
while a<3200:
    l.append(str(a))
    a += 7
    
# remove all numbers divisible by 5 from list
for i in l:
    if int(i)%5==0:
        b = l.index(i)
        del l[b::5]
        break
        
print(','.join(l))  