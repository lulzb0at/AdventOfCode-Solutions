# Path to your input file
input = ""

max = 0
cals = []
totals = []

with open(input,'r') as fh:
    lines = fh.read()
   
for line in lines.splintlines():
    if line.isdigit():
        cals.append(line)
    else:
        totals.append(sum(cals))
        if sum(cals) > max:
            max = sum(cals)
           
        cals = []
        
totals.sort()
answer = totals[-1] + totals[-2]+totals[-3]
