# 2048 Game

This project implements the classic 2048 board game for the final project of the Algorithm and Data Structure course.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Data Structures Used](#data-structures-used)
- [Algorithms](#algorithms)
- [Code Structure Explanation](#code-structure-explanation)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The 2048 Game project is a Python implementation of the popular 2048 puzzle game. The goal is to reach the 2048 tile by merging adjacent tiles of the same value.

## Features

- **Interactive Gameplay**: Use arrow keys to move tiles on the board.
- **Merge Functionality**: Merge tiles with the same value when moving in a specific direction.
- **Random Number Generator**: Spawn new tiles with random values.
- **Past Grid Tracking**: Keep track of the previous grid states using a stack.
- **Game Over and Victory Detection**: Detect when the game is over or when the player wins.

## Data Structures Used

- 2D Array: Representing the game grid.
- Stack (linked list-based): Storing past grid states.
- Dictionary: Managing key game features.

## Algorithms

- **Merge Algorithm**: Sum two cells adjacent in the same direction of movement.
- **Random Number Generator Algorithm**: Generate random numbers in the grid.
- **Move Algorithm**: Move the grid in the specified direction.

## Code Structure Explanation

## Code Structure Explanation

The code is organized into several components to enhance readability and maintainability.

### `GameBoard` Class

The `GameBoard` class is the core of the game logic and user interaction. It contains the following methods:

- **`__init__(self, size)`**: Initializes the game board with a specified size and sets up the initial grid with empty cells.

- **`update(self)`**: Prints the current state of the game grid to the terminal.

- **`read_user_input(self)`**: Listens for arrow key inputs using the `keyboard` library to determine the user's desired move direction.

- **`spawn_new(self)`**: Generates a new random number (2 or 4) in an empty cell on the grid.

- **`move(self, direction)`**: Moves the tiles on the grid in the specified direction (up, down, left, or right).

- **`merge(self, direction)`**: Merges adjacent tiles with the same value in the specified direction.

- **`is_game_over(self)`**: Checks if the game is over by verifying if there are any empty cells left on the grid.

- **`is_game_won(self)`**: Checks if the player has reached the 2048 tile, indicating a victory.

- **`past_grids(self, grid_to_push)`**: Pushes a copy of the current grid onto the `pastgrids` stack, allowing for undo functionality.

- **`check_invalid_move(self)`**: Checks if the current move is invalid (undo function). Restores the grid to the previous state if the move is invalid.

### `Stack` Class

The `Stack` class is a linked list-based implementation of a stack, used to store past grid states for undo functionality.

- **`push(self, item)`**: Adds an item to the top of the stack.

- **`pop(self)`**: Removes and returns the item from the top of the stack.

### Main Game Loop

The main game loop handles the overall flow of the game. It includes the following steps:

1. **Initialize the Game Board**: Create an instance of the `GameBoard` class with a specified size and spawn initial numbers.

2. **Main Loop Execution**: Continuously loop while the game is not over or the player has not won.

    - **Update**: Print the current state of the game grid.
    
    - **Save Past Grid**: Push a copy of the current grid onto the `pastgrids` stack.
    
    - **Read User Input**: Wait for and process the user's arrow key input.
    
    - **Move & Merge**: Execute the move and merge logic based on the user's input.

    - **Check Invalid Move**: Verify if the move is invalid (undo). If invalid, restore the grid to the previous state.
    
    - **Spawn New Number**: Generate a new random number on the grid.
    
    - **Print and Pause**: Print the updated grid and pause for a short duration for better visibility.
    
3. **Game Over or Victory**: When the loop exits, print the final state of the game grid and indicate whether the player won or the game is over.

This modular structure allows for easy understanding, testing, and potential future enhancements of the 2048 game implementation.


## How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/GRINGOLOCO7/2048Game.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install keyboard
    ```

3. **Run the Game:**
    ```bash
    python main.py
    ```

4. **Game Controls:**
    - Use arrow keys (up, down, left, right) to move tiles on the board.