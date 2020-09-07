x=input()
# c stores number of digits in original number
c=len(x)
n=int(x)
sq=n*n
#r gives the number at end of square with number of digits equal to c
r=sq%(10**c)
if(r==n):
    print("Number is automorphic")
else:
    print("Number is not automorphic")

