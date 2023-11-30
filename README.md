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
- **Score Tracking**: Each move the score get updated
- **Undo Function**: Allows players to revert to the previous grid state, facilitating strategic moves and error correction.
- **Game Over and Victory Detection**: Detect when the game is over or when the player wins.
- **Ranking System**: Maintaining a ranking of 10 most high scores.
- **Tree-Based Move Suggestions**: Provides approximate suggestions for optimal moves using a tree structure.

## Data Structures Used

- **2D Array**: Representing the game grid.
- **Stack** (linked list-based): Storing past grid states.
- **Dictionary**: Managing key game features.
- **Set**: Use a set to keep track of empty celleces (tiles with value 0)
- **Tree**: Used in the tree-based move suggestion system.

## Algorithms

- **Merge Algorithm**: Sum two cells adjacent in the same direction of movement.
- **Random Number Generator Algorithm**: Generate random numbers in the grid.
- **Move Algorithm**: Move the grid in the specified direction.
- **Sorting Algorithms (QuickSort)**: Used in ranking system to sort the high scores.

## Code Structure Explanation

The code is organized into several components to enhance readability and maintainability:

- **`main.py`**: The entry point of the game. It initializes the `GameBoard` and runs the main game loop.

- **`src` folder**: Contains various modules and classes:
  - **`game_class.py`**: Contains the `GameBoard` class with methods for game mechanics.
  - **`stack.py`**: Implements the `Stack` class for undo functionality.
  - **`tree_class.py`**: Defines the `TreePossibilities` class for move suggestions.
  - **`tree.py`**: Implements a tree with an array of children.



### `GameBoard` Class

The `GameBoard` class is the core of the game logic and user interaction. It contains the following methods:

- **`__init__(self, size)`**: Initializes the game board with a specified size ( 4 x 4 ) and sets up the initial grid with empty cells.

- **`initialize_empty_coordinates`**: Go troght all the grid as save the empty spaces in a set()
   - Time Complexity: O(n^2) - where n is the size of the grid. This method iterates through each cell of the grid.


- **`update(self)`**: Prints the current state of the game grid to the terminal.
  - Time Complexity: O(n^2) - as it iterates through each cell for printing.

- **`read_user_input(self)`**: Listens for arrow key inputs using the `keyboard` library to determine the user's desired move direction.

- **`spawn_new(self)`**: Generates a new random number (2 or 4) in an empty cell on the grid.
  - Time Complexity: O(1) - Random generation and placement.


- **`move(self, direction)`**: Moves the tiles on the grid in the specified direction (up, down, left, or right).
  - Time Complexity: O(n^2) - involves iterating through the grid to move tiles.


- **`merge(self, direction)`**: Merges adjacent tiles with the same value in the specified direction.
    - Time Complexity: O(n^2) - due to traversing and merging tiles in the grid.


- **`is_game_over(self)`**: Checks if the game is over by verifying if there are any empty cells left on the grid.
  - Time Complexity: O(n^2) - checks each cell of the grid.


- **`is_game_won(self)`**: Checks if the player has reached the 2048 tile, indicating a victory.
  - Time Complexity: O(n^2) - iterates through the grid to find the 2048 tile.


- **`past_grids(self, grid_to_push)`**: Pushes a copy of the current grid onto the `pastgrids` stack, allowing for undo functionality.

- **`check_invalid_move(self)`**: Checks if the current move is invalid (undo function). Restores the grid to the previous state if the move is invalid.

- **`undo(self)`**: Pop form the `pastgrids` Stack the previous state of the grid and restore it. It allow to go back to the previous move.
  - Time Complexity: O(1) - Stack pop operation is constant time.


- **`GAME(self)`**: **Main methiod** that loop until game is won or game is lost. It combine in the correct order all the previous methosds, showing the game to the user. 

### `Stack` Class

The `Stack` class is a **linked list-based** implementation of a stack, used to store past grid states for undo functionality.

- **`push(self, item, score)`**: Adds a grid and his related score to the top of the stack.
  - Time Complexity: O(1) - Inserting an item at the top of the stack is a constant time operation.


- **`pop(self)`**: Removes and returns the grid and score from the top of the stack.
  - Time Complexity: O(1) - Removing an item from the top of the stack is a constant time operation.


### `TreePossibilities` Class

The `TreePossibilities` class is responsible for generating a tree structure that represents possible future game states. It helps in suggesting the best move based on potential outcomes. The class includes the following methods:

- **`create_tree(self, depth)`**: Generates a tree of potential game states up to a specified depth. Each node represents a game state, and the tree branches represent possible moves from that state.
     - Time Complexity: 
        - Worst Case: Exponential, based on the depth and branching factor of the game states. The number of nodes grows exponentially with the depth of the tree.


- **`higher_values(self, root)`**: Traverses the tree starting from the root and identifies nodes that lead to higher game scores. It evaluates different paths to suggest the most promising move.
  - Time Complexity: 
    - Worst/Average Case: O(n) - where n is the number of nodes in the tree. The method traverses each node once.
- **`find_maxscore_in_direction(self, listOFadvice)`**: Analyzes the list of advised moves and their potential scores to determine the best possible move.
  - Time Complexity: 
    - Worst/Average Case: O(m) - where m is the length of the `listOFadvice`. The method iterates through each advised move to find the best one.




### Ranking System 
- Tracks high scores.
- Sorts scores using QuickSort and Bubble Sort.
- Top scores are stored and displayed to the user.

### Tree-Based Move Suggestion
- Provides the best move suggestions based on tree analysis.
- If a possibility of obtaining a higher score is detected, we suggest that move.

### Main Game Loop

The main game loop handles the overall flow of the game. It includes the following steps:

1. **Initialize the Game Board**: Create an instance of the `GameBoard` class with a specified size and spawn initial numbers.

2. **Main Loop Execution**: Afther calling **`GAME`** function: Continuously loop while the game is not over or the player has not won.

    - **Update**: Print the current state of the game grid.
    
    - **Save Past Grid**: Push a copy of the current grid onto the `pastgrids` stack.
    
    - **Read User Input**: Wait for and process the user's arrow key input.
    
    - **Move & Merge**: Execute the move and merge logic based on the user's input.

    - **Undo**: If 'u' is pressed it restore the grid to his previous status.

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
    ```bash
    pip install windows-curses
    ```

3. **Run the Game:**
    ```bash
    python main.py
    ```

4. **Game Controls:**
    - Use arrow keys (up, down, left, right) to move tiles on the board.
    - 'u' to undo
    - 'r' to view ranking
    - 'q' to quit
