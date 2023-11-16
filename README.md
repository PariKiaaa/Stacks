# Stacks Game

Stacks is a simple game implemented in Python using the Pygame library. The objective of the game is to stack bricks on top of each other as they move from right to left, trying to achieve the highest score possible.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [High Score](#high-score)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- Dynamic stacking of bricks.
- Colorful bricks with varying sizes.
- Sound effects for interactions.
- High score tracking.

## Installation

To run the game locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/PariKiaaa/Stacks.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Stacks
    ```

3. Install the required dependencies:

    ```bash
    pip install pygame
    ```

4. Run the game:

    ```bash
    python Stacks.py
    ```

## How to Play

- Move the stack left and right to align with incoming bricks.
- Press the space bar to drop the brick onto the stack.
- Aim to stack bricks perfectly to achieve a high score.

## Controls

- **Left Arrow:** Move the stack left.
- **Right Arrow:** Move the stack right.
- **Space Bar:** Drop the brick onto the stack.

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
