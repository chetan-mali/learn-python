def mutate_string(string, position, character):
    for i in range(0,len(string)):
        if (i==position):
            string[i]=character
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)