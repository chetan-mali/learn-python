number = "1,232,24,567,5544,33,23454"
new_number = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        new_number = number[i]
    print('{0}'.format(new_number), end='')
