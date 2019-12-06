import random

# Adults
adults = ['Papa', 'Mama', 'Andres', 'Pablo', 'Clara', 'Jaime', 'Ana', 'MJ', 'Nacho', 'Marina']
adults_exclusions = {'Pablo': ['Pablo', 'MJ'], 'Clara': ['Clara', 'Nacho'], 'Jaime': ['Jaime', 'Marina'], 'Papa': ['Papa', 'Mama'], 'Andres': ['Andres', 'Ana'],
                        'MJ': ['MJ', 'Pablo'], 'Nacho': ['Nacho', 'Clara'], 'Marina': ['Marina', 'Jaime'], 'Mama': ['Mama', 'Papa'], 'Ana': ['Ana', 'Andres']}
adults_results = {}

# Pairs & Children
children = {1: 'Nacho', 2: 'Elena', 3: 'Alonso', 4: 'Julia', 5: 'Irene', 6: 'Gonzalo'}
pairs = ['Pablo & MJ', 'Clara & Nacho', 'Jaime & Marina', 'Papa & Mama', 'Andres & Ana']
children_exclusions = {'Pablo & MJ': ['Elena', 'Irene'], 'Clara & Nacho': ['Nacho', 'Alonso'], 'Jaime & Marina': ['Julia', 'Gonzalo'], 'Papa & Mama': [], 'Andres & Ana': []}
children_results = {}

def throwdice_adults():
    dice = random.randint(0, 9)
    return adults[dice]

def throwdice_children():
    dice = random.randint(1, 6)
    return children[dice]

def throwdice_pairs():
    dice = random.randint(0, 4)
    return pairs[dice]

def run_adults():
    winners = []
    # Loop through Adults, each will get another adult assigned
    for adult in adults:
        winner = throwdice_adults()
        while winner in winners:
            print(f'{winner} is already assigned, throwing the dice again')
            winner = throwdice_adults()
        while winner in adults_exclusions[adult]:
            print(f'{winner} is excluded for adult {adult}, throwing the dice again')
            winner = throwdice_adults()

        winners.append(winner)
        print(f'==> {adult} assigned to {winner}')
        adults_results.update({adult: winner})

def run_children():
    winners = []
    # Loop through pairs, each will get a child assigned
    for pair in pairs:
        winner = throwdice_children()
        while winner in winners:
            print(f'{winner} is already assigned, throwing the dice again')
            winner = throwdice_children()
        while winner in children_exclusions[pair]:
            print(f'{winner} is excluded for pair {pair}, throwing the dice again')
            winner = throwdice_children()

        winners.append(winner)
        print(f'==> {pair} assigned to {winner}')
        children_results.update({pair: winner})

    # One extra random pair gets a second child assigned
    extra_pair = throwdice_pairs()
    winner = throwdice_children()
    while winner in winners:
        print(f'{winner} is already assigned, throwing the dice again')
        winner = throwdice_children()
    while winner in children_exclusions[extra_pair]:
        print(f'{winner} is excluded for pair {extra_pair}, throwing the dice again')
        winner = throwdice_children()

    print(f'==> {extra_pair} assigned to {winner}')
    children_results.update({extra_pair + ' extra': winner})

def run():
    run_adults()
    print(f'==> Adults Results: {adults_results}')

    run_children()
    print(f' Children Results: {children_results}')

run()