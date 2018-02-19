def sumofsquares(n):
    if n<0:
        return False;

    for i in range(1,int(n**(1/2))):
        for j in range(1,int(n*(1/2))):

            if i**2+j**2==n:
                return True;

    return False;
h = sumofsquares(32);
print(h);





