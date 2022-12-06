with open('input.txt','r') as fh: line = fh.read()

for i in range(len(line)):   
    print('%d: %s' % (i, line[i])) #
    if len(set(line[i:i+4])) == 4:
        print(i+4)
        break
