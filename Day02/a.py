A=1 # X - rock
B=2 # Y - paper
C=3 # Z - scissors

lose = 0
draw = 3
win = 6

# Path to your input file
input = ''

with open(input,'r') as fh:
    games = fh.readlines()

total = 0

for game in games:
    ## Opponent has rock
    if game.startswith('A'):
        if game.strip().endswith('X'):
            total += A + draw
        if game.strip().endswith('Y'):
            total += B + win
        if game.strip().endswith('Z'):
            total += C + lose
    ## Opponent has paper
    elif game.startswith('B'):
        if game.strip().endswith('X'):
            total += A + lose
        if game.strip().endswith('Y'):
            total += B + draw
        if game.strip().endswith('Z'):
            total += C + win
    ## Opponent has scissors
    elif game.startswith('C'):
        if game.strip().endswith('X'):
            total += A + win
        if game.strip().endswith('Y'):
            total += B + lose
        if game.strip().endswith('Z'):
            total += C + draw

print(total)
