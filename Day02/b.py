A=1 # X - rock      (need to lose)
B=2 # Y - paper     (need to draw)
C=3 # Z - scissors  (need to win )

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
        ## Need to lose
        if game.strip().endswith('X'):
            total += C + lose
        ## Need to draw
        if game.strip().endswith('Y'):
            total += A + draw
        ## Need to win
        if game.strip().endswith('Z'):
            total += B + win
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
            total += B + lose
        if game.strip().endswith('Y'):
            total += C + draw
        if game.strip().endswith('Z'):
            total += A + win

print(total)
