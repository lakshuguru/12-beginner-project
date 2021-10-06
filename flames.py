name1=list(input('enter the 1st name : ').lower())
name2=list(input('enter the 2nd name : ').lower())
n=[]
c=0
for i in name1:
    for j in name2:
        if i==j:
            name1.remove(i)
            name2.remove(j)

#print(name1)
#print(name2) 
n=name1+name2
print(n)
for l in n:
    c+=1
print(c)            
k=['f','l','a','m','e','s']            
print(len(k))
l=0
while len(k)>1:
    l=((c+l)%len(k))-1
    k.remove(k[l])
    print(k)