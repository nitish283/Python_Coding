def prob(l):
        min=l[0]
    
        for i in range(len(l)-1):
            k=l[i+1]-l[i]
            if(k>0):
                if(k<min):
                    min=k
                    n1=l[i]
                    n2=l[i+1]
            elif(-k<min):
                min=-k
                n1=l[i]
                n2=l[i+1]
        print(n1,n2)
        print(min)

x=input()
x=x+" "
k=""
l=[]
for i in range(len(x)):
	if(x[i]==' '):
		l.append(int(k))
		k=""
	else:
		k=k+x[i]
prob(l)
