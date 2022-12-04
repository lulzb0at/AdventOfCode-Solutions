with open('input.txt','r') as fh: lines = fh.read()

def get_seq(pair):
    return list(range( int(pair.split('-')[0]), int(pair.split('-')[1])+1))

total = 0

for line in lines.splitlines():   
    if set(get_seq(line.split(',')[0])) & set(get_seq(line.split(',')[1])):
        total += 1

print(total)
