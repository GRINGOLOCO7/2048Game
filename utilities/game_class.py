import sys
sys.path.append('2048Game\\utilities')
import random  # import random for spawning element in the grid
import curses  # for user input
import keyboard # for reading keyboard
import time  # for a delay from a move and another
from stack import Stack
from tree import TreeNode
from sort import QuickSort

class GameBoard:   # class that crete our gred... whill have many methods
    def __init__(self, size): # initialize
        self.size = size # size of grid that will be sizexsize
        self.grid = [[0] * size for _ in range(size)] # preallocate memory space for gid
        self.empty_cells =  self.initialize_empty_coordinates(self.grid) # create a set of tupples for ech value equal to 0 in the gred
        self.pastgrids = Stack() # initialize a stack to keep track of past grids
        self.score = 0  # initialize user score to 0

#########################################################################################

    def initialize_empty_coordinates(self, grid): # metod to find all value equal 0 in the grid andadd the to the set empty_celles
        empty_cells = set() # initialize empty_cells as a empty set
        for i in range(len(grid)): # go trough each row
            for j in range(len(grid[i])): # go trough each column
                if grid[i][j] == 0: # check condition... if the current element in the grid that we are watching is equal 0
                    empty_cells.add((i, j)) # add the cordinates in empty_cells
        return empty_cells # return empty_cells  --> "self.empty_cells =  self.initialize_empty_coordinates(self.grid)"

#########################################################################################

    def update(self, grid): # method that displays the current state of the game board
        for row in grid: #pass trough each row
            # Use join to add spaces between elements in each row
            row_str = '   '.join([f'{num:5}' for num in row]) # this is to don't make the grid shif when big numbers arrive
            # {num:5} is because 2048 is 4 digit, maximum possible number in the grid is 1024 and we dont wont the grid to shift
            # so we set fix space between numbers
            print(row_str) #print each tiles number with the corrrect and adjusted space btw the others
        print(f"Score: {self.score}") # print the current score

#########################################################################################

    def read_user_input(self): # Waits for and reads the user's input for direction or undo.
        # Define the keys for each direction and 'u' for undo
        direction_keys = {'left': 'left arrow', 'right': 'right arrow', 'up': 'up arrow', 'down': 'down arrow', 'undo': 'u', 'ranking': 'r', 'quit': 'q'}
        while True:  # while we don't get an input nothing will append and we will be stuck in this function
            for direction, key in direction_keys.items(): # Check for key events
                if keyboard.is_pressed(key): # detect if we pressed the current key
                    self.user_input = direction # save the value pressed inside the variable 'self.user_input'
                    return  # exit the loop

#########################################################################################

    def spown_new(self, grid, empty_cells): # method to spawn a new value that can be 2 or 4 in the empty cells
        # Define the possible outcomes and their corresponding weights
        outcomes = [2, 4] # # Define the possible outcomes and their corresponding weights
        weights = [9, 1]  # 90% chance of 2, 10% chance of 4
        # Use random.choices() to select a number based on the defined weights
        number = random.choices(outcomes, weights)[0] # it returns an array, that is why we add [0]
        empty_cells = self.initialize_empty_coordinates(grid) # track all empty cells (0) and save their cordinates as a set
        random_tuple = random.choice(tuple(empty_cells)) # Randomly select a tuple to chose a cordinate where we will put number
        row, column = random_tuple   # Unpack the tuple into separate variables
        empty_cells.remove((row, column)) # delete that cordinate from self.empty_cells
        #print(self.empty_cells)
        grid[row][column] = number # Place the new number in the randomly selected position

#########################################################################################

    def move(self, direction, grid):
        '''
        method to move the tiles in the inputed direction
        utill reached limit of the grid or another number diffrent than 0
        '''
        if direction == 'up': # check direction
            for row in range(self.size - 1, 0, -1): # for the row we start from bottom and go to the top -> this to avoid multiple merged in one moove
                for column in range(self.size):
                    if row == 0:
                        break
                    if grid[row-1][column] == 0:
                        grid[row][column], grid[row-1][column] = 0, grid[row][column]
        if direction == 'down':
            for row in range(self.size):
                for column in range(self.size):
                    if row == len(grid)-1:
                        break
                    if grid[row+1][column] == 0:
                        grid[row][column], grid[row+1][column] = 0, grid[row][column]
        if direction == 'left':
            for row in range(self.size):
                for column in range(self.size - 1, 0, -1):
                    if column == 0:
                        break
                    if grid[row][column - 1] == 0:
                        grid[row][column], grid[row][column - 1] = 0, grid[row][column]
        if direction == 'right':
            for row in range(self.size):
                for column in range(self.size):
                    if column == len(grid[row])-1:
                        break
                    if grid[row][column+1] == 0:
                        grid[row][column], grid[row][column+1] = 0, grid[row][column]

#########################################################################################

    def merge(self, direction, grid):
        '''
        method to merge the equel tiles according to the direction inputed
        '''
        merged_tiles = [[False] * self.size for _ in range(self.size)]  # Initialize a list to track merged tiles
        if direction == 'up':
            for col in range(self.size):
                for row in range(1, self.size):
                    if grid[row][col] != 0:
                        for r in range(row - 1, -1, -1):
                            if grid[r][col] == 0:
                                grid[r][col] = grid[r + 1][col]
                                grid[r + 1][col] = 0
                            elif grid[r][col] == grid[r + 1][col] and not merged_tiles[r][col] and not merged_tiles[r + 1][col]:
                                grid[r][col] *= 2
                                grid[r + 1][col] = 0
                                merged_tiles[r][col] = True
                                self.score += grid[r][col]
                                break
        if direction == 'down':
            for col in range(self.size):
                for row in range(self.size - 2, -1, -1):
                    if grid[row][col] != 0:
                        for r in range(row + 1, self.size):
                            if grid[r][col] == 0:
                                grid[r][col] = grid[r - 1][col]
                                grid[r - 1][col] = 0
                            elif grid[r][col] == grid[r - 1][col] and not merged_tiles[r][col] and not merged_tiles[r - 1][col]:
                                grid[r][col] *= 2
                                grid[r - 1][col] = 0
                                merged_tiles[r][col] = True
                                self.score += grid[r][col]
                                break
        if direction == 'right':
            for row in range(self.size):
                for col in range(self.size - 2, -1, -1):
                    if grid[row][col] != 0:
                        for c in range(col + 1, self.size):
                            if grid[row][c] == 0:
                                grid[row][c] = grid[row][c - 1]
                                grid[row][c - 1] = 0
                            elif grid[row][c] == grid[row][c - 1] and not merged_tiles[row][c] and not merged_tiles[row][c - 1]:
                                grid[row][c] *= 2
                                grid[row][c - 1] = 0
                                merged_tiles[row][c] = True
                                self.score += grid[row][c]
                                break
        if direction == 'left':
            for row in range(self.size):
                for col in range(1, self.size):
                    if grid[row][col] != 0:
                        for c in range(col - 1, -1, -1):
                            if grid[row][c] == 0:
                                grid[row][c] = grid[row][c + 1]
                                grid[row][c + 1] = 0
                            elif grid[row][c] == grid[row][c + 1] and not merged_tiles[row][c] and not merged_tiles[row][c + 1]:
                                grid[row][c] *= 2
                                grid[row][c + 1] = 0
                                merged_tiles[row][c] = True
                                self.score += grid[row][c]
                                break
        flattened_true_values = [value for row in merged_tiles for value in row if value is True]
        return flattened_true_values # will use to see if the game is game over or there stil are possible moves

#########################################################################################

    def update_ranking(self, score):

        file_path = "2048Game\\utilities\\ranking.txt"

        # Read numbers from the file
        with open(file_path, 'r') as file:
            numbers = file.readlines()

        # Convert each line to an integer and sort the list
        numbers = [int(num.strip()) for num in numbers]
        numbers.append(score)
        numbers = QuickSort(numbers)

        numbers = numbers[:10]

        with open(file_path, 'w') as file:
            for num in numbers:
                file.write(f"{num}\n")

#########################################################################################

    def display_ranking(self):

        file_path = "2048Game\\utilities\\ranking.txt"

        # Read numbers from the file
        with open(file_path, 'r') as file:
            numbers = file.readlines()

        numbers = [int(num.strip()) for num in numbers]
        for i in range(len(numbers)):
            print(f"{i+1}. {numbers[i]}")

#########################################################################################

    def is_game_over(self, grid, empty_cells): # method to check game over condition
        if empty_cells: # if the set 'empty_cells' is not empty
            return False # the game can contnue, we return false just for how the condition is formuled in the main loop
        directions = ['left', 'right', 'up', 'down'] # initialize all directions
        for dir in directions: # loop trough each possible direction
            copied_grid = [row[:] for row in grid] # create copy of the grid
            temp_grid = GameBoard(self.size) # create a gameboard istance
            temp_grid.grid = copied_grid # set the temporary grid equal to the given grid
            merged_occur = temp_grid.merge(dir, temp_grid.grid) # merge the grid in dir directions
            if merged_occur: # check if at least two tiles was merged
                return False # there is still a possible move => continume the game
            # if yes return false
        print("GAME OVER") # all empty cells are full and there are no more possible move
        self.update_ranking(self.score)
        self.display_ranking()
        return True # return true to end the loop => u lose

#########################################################################################

    def is_game_won(self): # method to check win condition
        for row in range(len(self.grid)): # go trough each row
            for column in range(len(self.grid[row])): # go trough each colum
                if self.grid[row][column] ==  2048: # check if ther is one value equal to 2048
                    print("YOW WIN")
                    return True # condition for win is acheved
        return False

#########################################################################################

    def past_grids(self, grid_to_push, score):
        '''
        method that saves the grid status in to a Stak
        It will be used for undo fuction and check for valid moves
        '''
        copied_grid = [row[:] for row in grid_to_push]  # make a copy of the grid so there is no relation with the game_board
        self.pastgrids.push(copied_grid, score) # pursh grid and score in to the stack

#########################################################################################

    def check_unvilid_move(self):
        '''
        method to check if mive is valid
        it means that if no tiles can move in that direction th emove is not allowed
        '''
        past__grid, score = self.pastgrids.pop() # pop last status of the grid
        if past__grid == self.grid: # if the last status of the grid is the same as current we have a faul move... we dont allow it
            print("No space for this move... try another direction")
            self.past_grids(past__grid, score) # add again the popped value
            return True
        self.past_grids(past__grid, score) # add again the popped value
        return False

#########################################################################################

    def undo(self):
        '''
        method to redo the move
        it restore the grid to his previous state in order to re-do the move
        '''
        # user pressed 'u'
        past__grid, past_score1 = self.pastgrids.pop() # pop the last grid stattus and score
        tuple_past = self.pastgrids.pop() # pop the past past grid value and score
        if not tuple_past:  # if the stack contained only one grid status => base state
            print('base state of grid reached')
            self.score = past_score1 # set score as last score
            self.grid = past__grid # set grid as the las grid
        else: # normal condition
            self.grid = tuple_past[0] # set grid as the las grid
            self.score = tuple_past[1] # set score as last score

#########################################################################################
