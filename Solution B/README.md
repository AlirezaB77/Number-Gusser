# Number Guessing Game

This is a Python-based number guessing game with a modular structure. The game generates a random number, and the player tries to guess it.

## Features

- Random number generation within a specified range
- Input validation
- Hint generation for incorrect guesses
- Score tracking

## How to Play

1. Run `main.py`
2. Enter a number between 1 and 100 when prompted
3. Receive hints for incorrect guesses
4. Keep guessing until you find the correct number

## Modules

- `input_valid.py`: Validates user input
- `number_gen.py`: Generates a random number
- `hint_gen.py`: Provides hints based on the user's guess
- `score.py`: Manages the scoring system

## Requirements

- Python 3.x

## Running the Game

## Notes

- The game uses a scoring system that decrements for each incorrect guess
- Hints are generated but currently commented out in the main loop

For detailed information on each module, refer to their respective docstrings.