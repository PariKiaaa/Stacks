# Stacks Game

Stacks is a simple game implemented in Python using the Pygame library. The objective of the game is to strategically push a moving brick onto a static stack. The player must carefully position the brick, ensuring that all parts are on the stack. Any part of the brick that extends beyond the stack will be removed, making the brick smaller. The game continues until the brick becomes too small to be visible or is completely pushed out of the stack.

## Table of Contents

- [How to Play](#how-to-play)
- [Controls](#controls)
- [High Score](#high-score)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## How to Play

- A brick moves from right to left across the screen.
- Press the space bar to push the brick onto the stack.
- Strategically position the brick to ensure all parts are on the stack.
- Any part of the brick extending beyond the stack will be removed.
- The game continues until the brick becomes too small to be visible or is completely pushed out of the stack.

## Controls

- **Space Bar:** Push the brick onto the stack.

## High Score

The game tracks your high score, which is stored in the `record.txt` file. Try to beat your own record and achieve the perfect stack!

## Project Structure

The main folder contains the following:

- `Stacks.py`: The main Python script for the game.
- `record.txt`: File to store the high score.
- `sounds/`: Folder containing sound files for the game.

## Dependencies

The game is built using the Pygame library. Make sure to install it before running the game:

```bash
pip install pygame
