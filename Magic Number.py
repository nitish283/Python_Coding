n=int(input())
s=n
while(s>=10):
    s=0
    while(n!=0):
        r=n%10;
        s+=r
        n=n//10
    n=s

if(s==1):
    print("Number is Magic Number")
else:
    print("Number is not a Magic Number")
