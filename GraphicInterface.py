from game2dboard import Board

import random
import curses  # for user input, pip install windows-curses
import keyboard
import time

class GameBoard:
    def __init__(self, size): # initialize
        self.size = size # size of grid that will be sizexsize
        self.grid = Board(size, size) # preallocate memory space for gid
        self.grid.title = "2048" # set title
        self.grid.grid_color = "gray" # set backgroun as gray
        self.grid.cell_size = 100       
        self.grid.cell_color = "bisque"

        self.empty_cells = [(row, column) for row in range(size) for column in range(size)]
    '''
#########################################################################################
    
    def read_user_input(self): #read the arrows form keyboard user
         while True:
            if keyboard.is_pressed('left'):
                self.user_input = 'left' # store the input arrow from user
                break
            elif keyboard.is_pressed('right'):
                self.user_input = 'right'
                break
            elif keyboard.is_pressed('down'):
                self.user_input = 'down'
                break
            elif keyboard.is_pressed('up'):
                self.user_input = 'up'
                break
            time.sleep(0.1)
    
#########################################################################################
    '''
    def spown_new(self): # function to spawn a new value that can be 2 or 4 in the empty cells
        # Define the possible outcomes and their corresponding weights
        outcomes = [2, 4]
        weights = [9, 1]  # 90% chance of 2, 10% chance of 4
        # Use random.choices() to select a number based on the defined weights
        number = random.choices(outcomes, weights)[0] # it returns an array, that is why we add [0]

        # track all empty cells (0) and save them in an array 
        # the 'empty_cells' array will contain cordinates for row and column
        self.empty_cells = [None] * (self.size * self.size)
        index = 0  # Index to update the empty_cells list
        for row in range(self.size):
            for column in range(self.size): # go trough each element in the array
                print(self.grid[row][column])
                if self.grid[row][column] ==  None:
                    self.empty_cells[index] = [row, column]
                    index += 1
        # Filter out the None values in the empty_cells list
        self.empty_cells = [cell for cell in self.empty_cells if cell is not None]
        # chose a cordinate where we will put number
        row, column = random.choice(self.empty_cells)
        # delete that cordinate from self.empty_cells
        self.empty_cells.remove([row, column])
        #print(self.empty_cells)

        # Place the new number in the selected position
        self.grid[row][column] = number
    '''   
#########################################################################################

    def move_up(self, val, row, column):
        merged_tiles = [[False] * self.size for _ in range(self.size)] # Initialize a list to track merged tiles for this move

        while row != 0: # given a row, we will go up untill it reach the row 0(top one) or a value diffrent than 0 in the tiles occur
            #print('row ', row)
            #print('colum ', column)
            #print('element above ', self.grid[row-1][column])
            if self.grid[row-1][column] == 0: # we can move up
                self.grid[row][column], self.grid[row-1][column] = 0, val # switch number with the above 0
                # Mark the tile as merged
                merged_tiles[row - 1][column] = True
            else: 
                #check if need to merge
                if self.grid[row-1][column] == self.grid[row][column] and not merged_tiles[row - 1][column]:
                    self.grid[row][column], self.grid[row-1][column] = 0, self.grid[row][column]+self.grid[row-1][column]  # switch with the merged number and replace a with a 0 in the position below
                    # Mark both tiles as merged
                    merged_tiles[row - 1][column] = True
                    merged_tiles[row][column] = True
                else:
                    pass
                break
            row -= 1
    def move_down(self, val, row, column):
        merged_tiles = [[False] * self.size for _ in range(self.size)]

        while row != len(self.grid)-1:
            if self.grid[row+1][column] == 0:
                self.grid[row][column], self.grid[row+1][column] = 0, val

                merged_tiles[row + 1][column] = True
            else: 
                #check if need to merge
                if self.grid[row+1][column] == self.grid[row][column] and not merged_tiles[row + 1][column]:
                    self.grid[row][column], self.grid[row+1][column] = 0, self.grid[row][column]+self.grid[row+1][column] 

                    merged_tiles[row + 1][column] = True
                    merged_tiles[row][column] = True
                else:
                    pass
                break
            row += 1
    def move_left(self, val, row, column):
        merged_tiles = [[False] * self.size for _ in range(self.size)]

        while column != 0:
            if self.grid[row][column-1] == 0:
                self.grid[row][column], self.grid[row][column-1] = 0, val
                
                merged_tiles[row][column-1] = True
            else: 
                #check if need to merge
                if self.grid[row][column-1] == self.grid[row][column] and not merged_tiles[row][column-1]:
                    self.grid[row][column], self.grid[row][column-1] = 0, self.grid[row][column]+self.grid[row][column-1]
                    
                    merged_tiles[row][column-1] = True
                    merged_tiles[row][column] = True 
                else:
                    pass
                break
            column -= 1
    def move_right(self, val, row, column):
        merged_tiles = [[False] * self.size for _ in range(self.size)]

        while column != len(self.grid[row])-1:
            if self.grid[row][column+1] == 0:
                self.grid[row][column], self.grid[row][column+1] = 0, val

                merged_tiles[row][column + 1] = True
            else: 
                #check if need to merge
                if self.grid[row][column+1] == self.grid[row][column] and not merged_tiles[row][column + 1]:
                    self.grid[row][column], self.grid[row][column+1] = 0, self.grid[row][column]+self.grid[row][column+1] 
                    
                    merged_tiles[row][column + 1] = True
                    merged_tiles[row][column] = True
                else:
                    pass
                break
            column += 1

#########################################################################################

    def is_game_over(self):
        if any(self.empty_cells):
            return False
        print("GAME OVER")
        return True

#########################################################################################

    def is_game_won(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] ==  2048:
                    print("YOW WIN")
                    return True
        return False

#########################################################################################





# initialize array
print("You can chose the size of your grid")
print("How much do you want ot challeng your-self?")
print("(Usually the grid is a 4x4)")
size = int(input("So... what is the size of the grid:\t"))
game_board = GameBoard(size)
game_board.spown_new()
game_board.spown_new()

# Main game loop
while not game_board.is_game_over() and not game_board.is_game_won():
    ### Handle user input and game logic

    # detect desire moovment
    game_board.read_user_input()
    #print(game_board.user_input)
    # move all tiles up
    for row in range(len(game_board.grid)):
        for column in range(len(game_board.grid[row])):
            if game_board.user_input == 'up':
                game_board.move_up(game_board.grid[row][column], row, column)
            if game_board.user_input == 'down':
                game_board.move_down(game_board.grid[len(game_board.grid)-1-row][column], len(game_board.grid)-1-row, column)
            if game_board.user_input == 'left':
                game_board.move_left(game_board.grid[row][column], row, column)
            if game_board.user_input == 'right':
                game_board.move_right(game_board.grid[row][len(game_board.grid[row])-1-column], row, len(game_board.grid[row])-1-column)

    # spown new number (2 or 4) in the grid
    game_board.spown_new()
    
    # pause the loop
    time.sleep(0.5)
    print('----------------')
'''

print("You can chose the size of your grid")
print("How much do you want ot challeng your-self?")
print("(Usually the grid is a 4x4)")
size = int(input("So... what is the size of the grid:\t"))
game_board = GameBoard(size)
game_board.spown_new()
game_board.spown_new()
game_board.grid.show()







