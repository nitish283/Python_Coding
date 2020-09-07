import copy
def perm(n):
        if(n==2):
                x=[[1,2],[2,1]]
                return(x)
        else:
                
                t=[]
                x=perm(n-1)
                b=copy.deepcopy(x)
                
                for i in range(len(x)):
                        for j in range(len(x[i])+1):
                                b[i].insert(j,n)
                                t.append(b[i])
                                b=copy.deepcopy(x)
                                
                return(t)       
N=int(input())
print((perm(N)))

