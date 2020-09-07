def rev(n):
               
        if(len(str(n))==1):
                return(n)
        else:
                rev(n//10)
                b=n%10
                rn=rn+b*(10**c)
                return(rn)


def reversDigits(num): 
    global rev_num 
    global base_pos 
    if(num > 0): 
        reversDigits((int)(num / 10)) 
        rev_num += (num % 10) * base_pos 
        base_pos *= 10
    return rev_num 
print(reversDigits(543))
