import random

def play(switch, num_doors=3):
    """
    Simulate a single game of the Monty Hall problem.

    Parameters:
        - switch: Boolean, whether or not your strategy is to switch doors
                  after the reveal.
        - num_doors: Integer, the number of doors in the game. Default is 3
                     for the classic game with 2 goats and 1 car.

    Returns:
        1 if you won, 0 if you lost
    """
    if not isinstance(num_doors, int) or num_doors < 3:
        raise ValueError('`num_doors` must be an integer greater than or equal to 3.')
    doors = ['car'] + ['goat'] * (num_doors - 1)
    random.shuffle(doors)

    initial_pick = random.choice(doors)

    if (initial_pick == 'goat' and switch) or (initial_pick == 'car' and not switch):
        return 1
    else:
        return 0

def simulate_games(num_games, switch, num_doors=3):
    """
    Simulate a multiple game of the Monty Hall problem.

    Parameters:
        - num_games: Integer, the number of games you want to simulate.
        - switch: Boolean, whether or not your strategy is to switch doors
                  after the reveal.
        - num_doors: Integer, the number of doors in the game. Default is 3
                     for the classic game with 2 goats and 1 car.

    Returns:
        1 if you won, 0 if you lost
    """
    if not isinstance(num_games, int) or num_games < 1:
        raise ValueError('`num_games` must be an integer greater than or equal to 1.')
    wins = 0
    for _ in range(num_games):
        wins += play(switch, num_doors)
    return f'winning percentage: {wins / num_games:.2%}'
