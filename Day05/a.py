stacks = {
    '1' : ['C', 'Z', 'N', 'B', 'M', 'W', 'Q', 'V'],
    '2' : ['H', 'Z', 'R', 'W', 'C', 'B'],
    '3' : ['F', 'Q', 'R', 'J'],
    '4' : ['Z', 'S', 'W', 'H', 'F', 'N', 'M', 'T'],
    '5' : ['G', 'F', 'W', 'L', 'N', 'Q', 'P'],
    '6' : ['L', 'P', 'W'],
    '7' : ['V', 'B', 'D', 'R', 'G', 'C', 'Q', 'J'],
    '8' : ['Z', 'Q', 'N', 'B', 'W'],
    '9' : ['H', 'L', 'F', 'C', 'G', 'T', 'J'],
    }

for line in lines.splitlines()[10:]:   
    crates = int(line.split()[1])
    src = line.split()[3]
    dst = line.split()[5]
    
    for _ in range(crates):
        stacks[dst].append(stacks[src].pop())

print(stacks)
