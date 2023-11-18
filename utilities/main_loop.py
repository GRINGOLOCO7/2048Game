import time
#from game_class import GameBoard 
from utilities.game_class import GameBoard 
#from create_tree import TreePossibilities 
from utilities.create_tree import TreePossibilities 


def GAME(game_board):
        game_board.spown_new()
        game_board.spown_new()
        invalidMove = False

        #########################################################################################

        # Main game loop
        while not game_board.is_game_over() and not game_board.is_game_won():
            ### Handle user input and game logic
            #####################################################################################
            
            # print the grid
            game_board.update()

            # detect desire moovment or undo function (u):
            game_board.read_user_input()

            #####################################################################################

            if not invalidMove:
                # save grid status in the game_board.pastgrids
                game_board.past_grids(game_board.grid, game_board.score)
            invalidMove = False

            #####################################################################################

            # move, merge, check for valid move or undo
            if game_board.user_input != 'undo':

                #################################################################################

                # move & merge
                # 1. move all in the direction pressed
                game_board.move(game_board.user_input)
                # 2. merge what needed
                game_board.merge(game_board.user_input)

                #################################################################################

                # check for fake move:
                # 1. if past grid is the same as the move after the canges (True), we don't spown new number
                if game_board.check_unvilid_move():
                    invalidMove = True
                else: #2. past grid is diffrent as current grid -> correct! spown new number
                    # spown new number (2 or 4) in the grid
                    game_board.spown_new()
                
                #################################################################################

            else: # user want to undo and go back to previous move
                game_board.undo()
            
            #####################################################################################

            # pause the loop
            time.sleep(0.5)
            print('----------------')

        #####################################################################################

        # Prnt last grid
        game_board.update()

#####################################################################################






'''
game_board = GameBoard(4)
GAME(game_board)
'''