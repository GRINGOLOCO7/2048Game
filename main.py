import random
import curses  # for user input, pip install windows-curses
import keyboard
import time

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def update(self):
        for el in self.grid:
            print(el)

    def move_tile(self):
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


    def merge_tiles(self, tile1, tile2):
        # Merge two tiles with the same value
        pass

    def is_game_over(self):
        # Check if the game is over
        pass

    def is_game_won(self):
        # Check if the player has won
        pass

# Main game loop
game_board = GameBoard(5)
while not game_board.is_game_over() and not game_board.is_game_won():
    ### Handle user input and game logic
    game_board.update()
    #while True:
    game_board.move_tile()
    print(game_board.user_input)