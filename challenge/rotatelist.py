def rotatelist(n,m):
    for i in range(0,m):
        n[1:len(n)+1]=n[0:len(n)];
        n[0] = n[-1];
        n = n[:len(n)-1]

    print(n);

rotatelist([1,2,3],1);
