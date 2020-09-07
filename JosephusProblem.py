n=int(input("Enter total number of prisoners"))
k=int(input("Enter k"))
l=[]
j=[]
for i in range(1,n+1):
     l.append(i)
x=len(l)
i=0
while(len(l)>1):
    i=(i+k-1)%len(l)
    l.remove(l[i])
    
print(l)

