import os

# path to your inpout file
input="" 

with open(input,'r') as fh:
    lines = fh.read()
    
total = []

for line in lines.splitlines():   
    letter = ( set(line[:int( len(line) /2 ) ]) & set(line[int( len(line) /2 ) :])).pop()    
    if letter.islower():
        total.append(ord(letter)-96)    
    else:
        total.append(ord(letter)-38)

print(sum(total))
