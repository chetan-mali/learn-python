def sumSquare(n):
    i = 0;
    while i * i <= n:
        j = 0;
        while (j * j <= n):
            if (i * i + j * j == n):
                return True;
            j = j + 1;
        i = i + 1;

    return False


# driver Program
m=sumSquare(0);
print(m);