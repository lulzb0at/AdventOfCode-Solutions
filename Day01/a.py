# Path to your input file
input = ""

max = 0
cals = []

with open(input,'r') as fh:
    lines = fh.read()
   
for line in lines.splintlines():
    if line.isdigit():
        cals.append(line)
    else:
        if sum(cals) > max:
            max = sum(cals)
        cals = []
        
print(max)
