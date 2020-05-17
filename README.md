# Connect 4!

This is the popular game Connect 4 built with Python and PyGame. In this game, you play against an agent
that decides moves using the MiniMax algorithm. The algorithm uses alpha-beta pruning to speed up decisions. It also rewards/penalizes wins/losses made with fewer moves to go for the win quickly.

## Running the Game

You will need [pipenv](https://github.com/pypa/pipenv) and [pyenv](https://github.com/pyenv/pyenv) (or Python 3.8 already installed).

```
pipenv install
pipenv run python main.py
```

## Running Simulated Games

There is also an option to run a series of game simulations, which pits the MiniMax agent against an agent that just makes random moves (assuming they are valid). You can run the simulations by:

```
pipenv run python main.py --sim [n]
```

where `n` is how many games you want to run (default 10).

## Future Work

Add a reinforcement learning agent and compare it to the MiniMax agent using the game simulations.
