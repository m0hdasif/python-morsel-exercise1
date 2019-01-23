# Random Fun
Random things in Python.

## Requirements
Python 3

## Contents
1. Monty Hall Problem simulator:
    - You are given a choice of 3 doors behind one of which is a car; the other 2 have goats. After you pick one, the host shows you what is behind the other door--which will always be a goat. You are then given the option to switch, but should you?
    - Turns out that you should always switch! In the case of 3 doors, you have a 2/3 chance of winning if you switch.
    - This can be extended to many more doors where all but one door contains a goat. In which case, you will be left to choose between the one you choose and the single other closed door.
    - Try out the simulator to see if for yourself!

    ```
    >>> import monty_hall as mh

    # find your winning percentage in 1000 games with the switch strategy
    >>> mh.simulate_games(1000, True)
    'winning percentage: 66.70%'

    # find your winning percentage in 1000 games with the switch strategy on 100 doors
    >>> mh.simulate_games(1000, True, 1000)
    'winning percentage: 99.30%'
    ```
