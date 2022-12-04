# path to input file
inpout = ''

with open(input,'r') as fh:
    lines = fh.read()
   
total = []

for line in lines.splitlines():  
    letter = ( set(line[:int( len(line) /2 ) ]) & set(line[int( len(line) /2 ) :])).pop()
    total.append(ord(letter)-96) if letter.islower() else total.append(ord(letter)-38)

print(sum(total))
