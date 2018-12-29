import random

children = {1: 'Nacho', 2: 'Elena', 3: 'Alonso', 4: 'Julia', 5: 'Irene'}
pairs = ['Pablo & MJ', 'Andres & Julia', 'Andres & Ana', 'Clara & Nacho', 'Jaime & Marina']
exclusions = {'Pablo & MJ': ['Elena', 'Irene'], 'Clara & Nacho': ['Nacho', 'Alonso'], 'Jaime & Marina': ['Julia'], 'Andres & Julia': [], 'Andres & Ana': []}
results = {}

def throwdice():
    dice = random.randint(1, 5)
    return children[dice]

def run():
    winners = []
    for pair in pairs:
        winner = throwdice()
        while winner in winners:
            #print (winner, 'is already selected, throwing the dice again')
            winner = throwdice()
        while winner in exclusions[pair]:
            #print (winner, 'is excluded for pair', pair, ', throwing the dice again')
            winner = throwdice()

        winners.append(winner)
        #print(pair, " -> ", winner)
        results.update({pair: winner})

    print('=>>', winners)
    return tuple(winners)

#combined = set()
#for x in range(100):
#    combined.add(run())
#print(combined)

run()
print(results)