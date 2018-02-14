ip_address = input('Type an IP address : ')
ip_address += '.'
flag = 0
flag1 = 1
len1 = len(ip_address)

for i in range(0, len1):
    if ip_address[i] in '0123456789':
        flag = flag + 1

    if ip_address[i] == '.':
        print('Length of segment {0} is {1}'.format(flag1, flag))
        flag = 0
        flag1 += 1
