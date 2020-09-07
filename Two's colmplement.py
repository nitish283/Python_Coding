#The two's complement of a positive number X is equivalent to binary representation of -X.
#Therefore, to find the two's complement of -X, we simply take one's complement of user input and add '1' to it.

x=input()  #binary input = two's complement of X
t=[]    # to store one's complement of input
c=0

for i in range(len(x)):
    if x[i]=='0':
        t.append('1')
    else:
        t.append('0')
        c=1
if(c!=1):
    t=['0']+t
print(t)
i=len(t)-1

while(i>=0):      #adding 1 
    if(t[i]=='1'):
        t[i]='0'
    else:
        t[i]='1'
        break
    i-=1
print(''.join(t))

