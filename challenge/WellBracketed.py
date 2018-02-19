def wellbraketed(n):
    flag=0;
    for i in n:

        if i=='(':
           flag=flag+1;
        if i==')' :
            if flag>=1:
                flag=flag-1;
            else:
                return False;

    if flag==0:
        return True;
    else:
        return False;


print(wellbraketed("(a+b)"));
print(wellbraketed("a+b)("));
print(wellbraketed("a+b)"));
