import random
import curses  # for user input, pip install windows-curses
import keyboard
import time
#from stack import Stack 
from utilities.stack import Stack

class GameBoard:
    def __init__(self, size): # initialize
        self.size = size # size of grid that will be sizexsize
        self.grid = [[0] * size for _ in range(size)] # preallocate memory space for gid
        self.empty_cells =  self.initialize_empty_coordinates()
        self.pastgrids = Stack()
        self.score = 0

#########################################################################################

    def initialize_empty_coordinates(self):
        empty_cells = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    empty_cells.add((i, j))
        return empty_cells

#########################################################################################
    
    def update(self): # function that print on terminal the grid
        """
        Displays the current state of the game board.
        """
        for row in self.grid: #pass trough each row
            # Use join to add spaces between elements in each row
            row_str = '   '.join([f'{num:5}' for num in row]) # this is to don't make the grid shif when big numbers arrive
            print(row_str) #print each tiles number with the corrrect and adjusted space btw the others
        print(f"Score: {self.score}")

#########################################################################################
    
    def read_user_input(self):
        """
        Waits for and reads the user's input for direction or undo.
        """
        # Define the keys for each direction
        direction_keys = {'left': 'left arrow', 'right': 'right arrow', 'up': 'up arrow', 'down': 'down arrow', 'undo': 'u'}
        while True:
            # Check for key events
            for direction, key in direction_keys.items():
                if keyboard.is_pressed(key):
                    self.user_input = direction
                    return
            time.sleep(0.1)
    
#########################################################################################

    def spown_new(self): 
        '''
        method to spawn a new value that can be 2 or 4 in the empty cells
        '''
        # Define the possible outcomes and their corresponding weights
        outcomes = [2, 4]
        weights = [9, 1]  # 90% chance of 2, 10% chance of 4
        # Use random.choices() to select a number based on the defined weights
        number = random.choices(outcomes, weights)[0] # it returns an array, that is why we add [0]
        # track all empty cells (0) and save them in an array 
        # the 'empty_cells' set will contain cordinates for row and column
        self.empty_cells = self.initialize_empty_coordinates()
        # chose a cordinate where we will put number
        # Randomly select a tuple
        random_tuple = random.choice(tuple(self.empty_cells))
        # Unpack the tuple into separate variables
        row, column = random_tuple        
        # delete that cordinate from self.empty_cells
        self.empty_cells.remove((row, column))
        #print(self.empty_cells)
        # Place the new number in the selected position
        self.grid[row][column] = number
    
#########################################################################################
  
    def move(self, direction):
        '''
        method to move the tiles in the inputed direction 
        utill reached limit of the grid or another number diffrent than 0
        '''
        if direction == 'up':
            for row in range(self.size - 1, 0, -1):
                for column in range(self.size):
                    if row == 0:
                        break
                    if self.grid[row-1][column] == 0:
                        self.grid[row][column], self.grid[row-1][column] = 0, self.grid[row][column]
        if direction == 'down':
            for row in range(self.size):
                for column in range(self.size):
                    if row == len(self.grid)-1:
                        break
                    if self.grid[row+1][column] == 0:
                        self.grid[row][column], self.grid[row+1][column] = 0, self.grid[row][column]
        if direction == 'left':
            for row in range(self.size):
                for column in range(self.size - 1, 0, -1):
                    if column == 0:
                        break
                    if self.grid[row][column - 1] == 0:
                        self.grid[row][column], self.grid[row][column - 1] = 0, self.grid[row][column]
        if direction == 'right':
            for row in range(self.size):
                for column in range(self.size):
                    if column == len(self.grid[row])-1:
                        break
                    if self.grid[row][column+1] == 0:
                        self.grid[row][column], self.grid[row][column+1] = 0, self.grid[row][column]
    
#########################################################################################
    
    def merge(self, direction):
        '''
        method to merge the equel tiles according to the direction inputed
        '''
        merged_tiles = [[False] * self.size for _ in range(self.size)]  # Initialize a list to track merged tiles     
        if direction == 'up':
            for col in range(self.size):
                for row in range(1, self.size):
                    if self.grid[row][col] != 0:
                        for r in range(row - 1, -1, -1):
                            if self.grid[r][col] == 0:
                                self.grid[r][col] = self.grid[r + 1][col]
                                self.grid[r + 1][col] = 0
                            elif self.grid[r][col] == self.grid[r + 1][col] and not merged_tiles[r][col] and not merged_tiles[r + 1][col]:
                                self.grid[r][col] *= 2
                                self.grid[r + 1][col] = 0
                                merged_tiles[r][col] = True
                                self.score += self.grid[r][col]
                                break
        if direction == 'down':
            for col in range(self.size):
                for row in range(self.size - 2, -1, -1):
                    if self.grid[row][col] != 0:
                        for r in range(row + 1, self.size):
                            if self.grid[r][col] == 0:
                                self.grid[r][col] = self.grid[r - 1][col]
                                self.grid[r - 1][col] = 0
                            elif self.grid[r][col] == self.grid[r - 1][col] and not merged_tiles[r][col] and not merged_tiles[r - 1][col]:
                                self.grid[r][col] *= 2
                                self.grid[r - 1][col] = 0
                                merged_tiles[r][col] = True
                                self.score += self.grid[r][col]
                                break
        if direction == 'right':
            for row in range(self.size):
                for col in range(self.size - 2, -1, -1):
                    if self.grid[row][col] != 0:
                        for c in range(col + 1, self.size):
                            if self.grid[row][c] == 0:
                                self.grid[row][c] = self.grid[row][c - 1]
                                self.grid[row][c - 1] = 0
                            elif self.grid[row][c] == self.grid[row][c - 1] and not merged_tiles[row][c] and not merged_tiles[row][c - 1]:
                                self.grid[row][c] *= 2
                                self.grid[row][c - 1] = 0
                                merged_tiles[row][c] = True
                                self.score += self.grid[row][c]
                                break
        if direction == 'left':
            for row in range(self.size):
                for col in range(1, self.size):
                    if self.grid[row][col] != 0:
                        for c in range(col - 1, -1, -1):
                            if self.grid[row][c] == 0:
                                self.grid[row][c] = self.grid[row][c + 1]
                                self.grid[row][c + 1] = 0
                            elif self.grid[row][c] == self.grid[row][c + 1] and not merged_tiles[row][c] and not merged_tiles[row][c + 1]:
                                self.grid[row][c] *= 2
                                self.grid[row][c + 1] = 0
                                merged_tiles[row][c] = True
                                self.score += self.grid[row][c]
                                break


#########################################################################################

    def is_game_over(self):
        '''
        method to check game over condition
        '''
        if self.empty_cells:
            return False
        print("GAME OVER")
        return True

#########################################################################################

    def is_game_won(self):
        '''
        method to check win condition
        '''
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] ==  2048:
                    print("YOW WIN")
                    return True
        return False

#########################################################################################

    def past_grids(self, grid_to_push, score):
        '''
        method that saves the grid status in to a Stak
        It will be used for undo fuction and check for valid moves
        '''
        copied_grid = [row[:] for row in grid_to_push]       
        self.pastgrids.push(copied_grid, score)

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
        print('Move delition...')
        past__grid, past_score1 = self.pastgrids.pop()
        tuple_past = self.pastgrids.pop()
        if not tuple_past:  # if the stack contained only one grid status => base state
            print('base state of grid reached')
            self.score = past_score1
            self.grid = past__grid
        else: # normal condition
            self.grid = tuple_past[0]
            self.score = tuple_past[1]

#########################################################################################

