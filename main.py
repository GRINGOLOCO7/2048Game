import random
import curses  # for user input, pip install windows-curses
import keyboard
import time

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.empty_cells = [1] * (size * size) # it is 1 becaus eif all are 0 it is game over

#########################################################################################
    
    def update(self):
        for row in self.grid:
            # Use join to add spaces between elements in each row
            row_str = '   '.join([f'{num:5}' for num in row]) # this is to don't make the grid shif when big numbers arrive
            print(row_str)

#########################################################################################
    
    def read_user_input(self):
         while True:
            if keyboard.is_pressed('left'):
                self.user_input = 'left'
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

    def spown_new(self):
        # Define the possible outcomes and their corresponding weights
        outcomes = [2, 4]
        weights = [9, 1]  # 90% chance of 2, 10% chance of 4
        # Use random.choices() to select a number based on the defined weights
        number = random.choices(outcomes, weights)[0]

        # track all empty cells (0) and save them in an array 
        # the 'empty_cells' array will contain cordinates for row and column
        self.empty_cells = [None] * (self.size * self.size)
        index = 0  # Index to update the empty_cells list
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if self.grid[row][column] ==  0:
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
    
#########################################################################################

    def move_up(self, val, row, column):
        while row != 0:
            #print('row ', row)
            #print('colum ', column)
            #print('element above ', self.grid[row-1][column])
            if self.grid[row-1][column] == 0:
                self.grid[row][column], self.grid[row-1][column] = 0, val
            else: 
                #check if need to merge
                if self.grid[row-1][column] == self.grid[row][column]:
                    self.grid[row][column], self.grid[row-1][column] = 0, self.grid[row][column]+self.grid[row-1][column] 
                else:
                    pass
                break
            row -= 1
    def move_down(self, val, row, column):
        while row != len(self.grid)-1:
            if self.grid[row+1][column] == 0:
                self.grid[row][column], self.grid[row+1][column] = 0, val
            else: 
                #check if need to merge
                if self.grid[row+1][column] == self.grid[row][column]:
                    self.grid[row][column], self.grid[row+1][column] = 0, self.grid[row][column]+self.grid[row+1][column] 
                else:
                    pass
                break
            row += 1
    def move_left(self, val, row, column):
        while column != 0:
            if self.grid[row][column-1] == 0:
                self.grid[row][column], self.grid[row][column-1] = 0, val
            else: 
                #check if need to merge
                if self.grid[row][column-1] == self.grid[row][column]:
                    self.grid[row][column], self.grid[row][column-1] = 0, self.grid[row][column]+self.grid[row][column-1] 
                else:
                    pass
                break
            column -= 1
    def move_right(self, val, row, column):
        while column != len(self.grid[row])-1:
            if self.grid[row][column+1] == 0:
                self.grid[row][column], self.grid[row][column+1] = 0, val
            else: 
                #check if need to merge
                if self.grid[row][column+1] == self.grid[row][column]:
                    self.grid[row][column], self.grid[row][column+1] = 0, self.grid[row][column]+self.grid[row][column+1] 
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
    # print the grid
    game_board.update()

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
game_board.update()