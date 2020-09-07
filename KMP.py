x=input("Enter original:")
s=input("Enter substring:")
l=[0]*len(s)
c=0
i=0
j=1

while(j<len(s)):
    if(s[j]==s[c]):
        c+=1
        l[j]=c
        j+=1
    else:
        if(c!=0):
            c=l[c-1]
        else:
            l[j]=0
            j+=1

j=0
while(i<len(x)):
    if s[j]==x[i]:
        i+=1
        j+=1

    if(j==len(s)):
        print("match at:",(i-j))
        j=l[j-1]

    elif i<len(x) and s[j]!= x[i]:
        if(j!=0):
            j=l[j-1]
        else:
            i+=1

    
