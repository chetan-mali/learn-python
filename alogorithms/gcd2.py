#euclids algorithm

def gcd(m,n):

    if n>m :
        (m,n) = (n,m)

    if (m%n)==0:
        return(n)
    else:
        return(gcd((n,m%n)))


j = gcd(13,26)
print(j)