with open('input.txt','r') as fh: lines = fh.read()

max = 0
cals = []
   
for line in lines.splintlines():
    if line.isdigit():
        cals.append(line)
    else:
        if sum(cals) > max:
            max = sum(cals)
        cals = []
        
print(max)
