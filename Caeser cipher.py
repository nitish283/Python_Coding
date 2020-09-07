import string

def encrypt_this(x,k):
    f=open(x)
    w=open("sherlock_encrypted.txt","w+")
    s=f.read()
    s=s.lower()
    l=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while(k>26):
        k=k%26
    
    temp=""
    for i in range(len(s)):
        if(s[i]=="\n"):
            w.write(temp)
            w.write("\n")
            temp=""
        else:
            b=l.index(s[i])
            b=b+k
            if(b>26):
                b=b-26
            temp=temp+l[b]
        
    f.close()
    w.close()

def cryptanalyse(x):
    f=open(x)
    
    l=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=f.read()
    d=open("Dict.txt", "r")
    dr=d.read().split('\n')
    w=open("sherlock_decrypt.txt","w+")
    ll=[]
    c=0
    for j in range(1,26):
            temp=""
            for i in range(len(s)):
                if(s[i]=="\n"):
                    for nn in range(len(dr)):
                        if (dr[nn]==temp):
                            c+=1
                
                    temp=""
                else:
                    temp=temp+s[i]
            ll.append(c)
    max=ll[0]
    for nnn in range(len(ll)):
        if(ll[nnn]>max):
            max=ll[nnn]
    temp=""
    for i in range(len(s)):
        if(s[i]=="\n"):
            w.write(temp)
            w.write("\n")
            temp=""
        else:
            b=l.index(s[i])
            b=b+max
            if(b>26):
                b=b-26
            temp=temp+l[b]
    return(max)
    f.close()
    d.close()
    w.close()
cryptanalyse("sherlock_encrypted.txt")