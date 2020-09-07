def msa(a):
        x=[]
        ms=000
        endsum=000

        for i in range(1,len(a)):
                if(a[i]>endsum+a[i]):
                        endsum=a[i]
                else:
                        endsum=endsum+a[i]
                
                if(ms<endsum):
                        ms=endsum
        print(ms)

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
msa(l)
