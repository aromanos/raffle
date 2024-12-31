import random

# Adults
adults = ['Andres', 'Pablo', 'Clara', 'Jaime', 'Ana', 'MJ', 'Nacho', 'Marina']
adults_exclusions = {'Pablo': ['Pablo', 'MJ'], 'Clara': ['Clara', 'Nacho'], 'Jaime': ['Jaime', 'Marina'], 'Andres': ['Andres', 'Ana'],
                        'MJ': ['MJ', 'Pablo'], 'Nacho': ['Nacho', 'Clara'], 'Marina': ['Marina', 'Jaime'], 'Ana': ['Ana', 'Andres']}

# Pairs & Children
children = {1: 'Nacho', 2: 'Elena', 3: 'Alonso', 4: 'Julia', 5: 'Irene', 6: 'Gonzalo'}
pairs = ['Pablo & MJ', 'Clara & Nacho', 'Jaime & Marina', 'Andres & Ana']
children_exclusions = {'Pablo & MJ': ['Elena', 'Irene'], 'Clara & Nacho': ['Nacho', 'Alonso'], 'Jaime & Marina': ['Julia', 'Gonzalo'], 'Andres & Ana': []}

def throwdice_adults():
    dice = random.randint(0, 7)
    return adults[dice]

def throwdice_children():
    dice = random.randint(1, 6)
    return children[dice]

def throwdice_pairs():
    dice = random.randint(0, 3)
    return pairs[dice]

def run_adults():
    results = {}
    winners = set()  # Use a set for faster membership checks

    for adult in adults:
        max_retries = 100  # Prevent infinite loops
        retries = 0

        while True:
            winner = throwdice_adults()
            retries += 1

            if retries > max_retries:
                raise RuntimeError(f"Unable to find a valid winner for {adult} after {max_retries} retries")

            if winner in winners:
                print(f"{winner} is already assigned, throwing the dice again")
                continue

            if winner in adults_exclusions.get(adult, []):
                print(f"{winner} is excluded for adult {adult}, throwing the dice again")
                continue

            # Valid winner found
            winners.add(winner)
            print(f"==> {adult} assigned to {winner}")
            results[adult] = winner
            break  # Exit the loop and move to the next adult

    return results


def run_children():
    results = {}
    winners = []
    winner_pairs = []
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
        results.update({pair: winner})

    # One extra random pair excluding Ana & Andres gets a second child assigned
    extra_pair = throwdice_pairs()
    while extra_pair == 'Andres & Ana':
        print(f'{winner} cannot be Andres & Ana, throwing the dice again')
        extra_pair = throwdice_pairs()

    winner = throwdice_children()
    while winner in winners:
        print(f'{winner} is already assigned, throwing the dice again')
        winner = throwdice_children()
    while winner in children_exclusions[extra_pair]:
        print(f'{winner} is excluded for pair {extra_pair}, throwing the dice again')
        winner = throwdice_children()

    winners.append(winner)
    winner_pairs.append(extra_pair)
    print(f'==> {extra_pair} extra assigned to {winner}')
    results.update({extra_pair + ' extra': winner})

    # Ana & Andres always get a second child assigned
    another_extra_pair = 'Andres & Ana'
    winner = throwdice_children()
    while winner in winners:
        print(f'{winner} is already assigned, throwing the dice again')
        winner = throwdice_children()
    while winner in children_exclusions[another_extra_pair]:
        print(f'{winner} is excluded for pair {another_extra_pair}, throwing the dice again')
        winner = throwdice_children()

    winners.append(winner)
    winner_pairs.append(another_extra_pair)
    print(f'==> {another_extra_pair} another assigned to {winner}')
    results.update({another_extra_pair + ' another': winner})
    return results

def main():
    adults_results = run_adults()
    print(f'==> Adults Results: {adults_results}')

    #children_results = run_children()
    #print(f'==> Children Results: {children_results}')

if __name__ == '__main__':
    main()