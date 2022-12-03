# path to your inpout file
filepath = ""

with open(filepath,'r') as fh:
    lines = fh.read()
    
total = []

for a,b,c in zip(*[iter(lines.splitlines())]*3):   
    letter = (set(a.strip()) & set(b.strip()) & set(c.strip())).pop()
    if letter.islower():
        total.append(ord(letter)-96)    
    else:
        total.append(ord(letter)-38)

print(sum(total))
