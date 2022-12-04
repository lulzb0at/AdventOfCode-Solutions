input = "" # path to your inpout file
with open(input,'r') as fh: lines = fh.read()
    
total = []
for a,b,c in zip(*[iter(lines.splitlines())]*3):   
    letter = (set(a.strip()) & set(b.strip()) & set(c.strip())).pop()
    total.append(ord(letter)-96) if letter.islower() else total.append(ord(letter)-38)
print(sum(total))
