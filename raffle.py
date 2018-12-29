import random

children = {1: 'nacho', 2: 'elena', 3: 'alonso', 4: 'julia', 5: 'irene'}
pairs = ['Pablo & MJ', 'Andres & Julia', 'Andres & Ana', 'Clara & Nacho', 'Jaime & Marina']
winners = []

for pair in pairs:
    
    dice = random.randint(1, 5)
    winner = children[dice]
    while winner in winners:
        print (winner, ' is already selected, throwing the dice again')
        dice = random.randint(1, 5)
        winner = children[dice]

    winners.append(winner)
    print(pair, " -> ", winner)

print(winners)