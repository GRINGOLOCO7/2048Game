import sys
sys.path.append('2048Game\\utilities')
import time
from colorama import Fore, Style # for fancy print statments
from game_class import GameBoard
from tree_class import TreePossibilities
import copy


def GAME(game_board, levels_for_tree_suggestion):
        game_board.spown_new(game_board.grid, game_board.empty_cells) # spawn first 2 number to start
        game_board.spown_new(game_board.grid, game_board.empty_cells)

        #####################################################################################

        invalidMove = False # invalid move set to false

        #####################################################################################

        # calculate the empty cells
        game_board.empty_cells = game_board.initialize_empty_coordinates(game_board.grid) # find cells with value 0

        #########################################################################################

        # Main game loop
        while not game_board.is_game_over(game_board.grid, game_board.empty_cells) and not game_board.is_game_won(): # continue untill game over or game win
            ### Handle user input and game logic
            #####################################################################################

            # creat tree aff all possibilities and advice best move in order to achive higher score
            advice = None
            tree = TreePossibilities(game_board.grid)
            root = tree.create_tree(levels_for_tree_suggestion)
            listOFadvice = tree.higher_values(root)
            #print(f"list of advice: {listOFadvice}")
            copied_grid = [row[:] for row in game_board.grid]
            temp_board = GameBoard(game_board.size)
            temp_board.grid = copy.deepcopy(copied_grid)
            while not advice:
                advice = tree.find_maxscore_in_direction(listOFadvice)
                temp_board.move(advice, temp_board.grid)
                temp_board.merge(advice, temp_board.grid)
                #print(f"temp board: {temp_board.grid}, copied grid: {copied_grid}")
                if temp_board.grid == copied_grid:
                    listOFadvice = [tup for tup in listOFadvice if tup[0] != advice]
                    advice = None
                    #print(f"list of advice: {listOFadvice}")
                    if not listOFadvice:
                        advice = 'I think you lost...'

            print(f"Our approximated suggestion tree advice to move {Fore.GREEN}{Style.BRIGHT}{advice}{Style.RESET_ALL} to achive higer score")

            #####################################################################################

            # print the grid to terminal so user can see it
            game_board.update(game_board.grid)

            # detect desire moovment or undo (u)
            game_board.read_user_input()

            #####################################################################################

            if not invalidMove:  # so if we do an invalid move we dont store two consecutive same grids
                game_board.past_grids(game_board.grid, game_board.score) # save grid status in the game_board.pastgrids
            invalidMove = False # invalid move set to false

            #####################################################################################
            # display ranking is r is pressed
            if game_board.user_input == 'ranking':
                game_board.display_ranking(game_board.score)
                invalidMove = True # so we dont store two consecutive same grids

            #####################################################################################
            # quit if q is pressed
            elif game_board.user_input == 'quit':
                game_board.update_ranking(game_board.score)
                game_board.display_ranking(game_board.score)
                print("You give up")
                break


            #####################################################################################
            # move, merge, check for valid move or undo
            elif game_board.user_input != 'undo': # we want to move

                #################################################################################

                # move & merge
                # 1. move all in the direction pressed
                game_board.move(game_board.user_input, game_board.grid)
                # 2. merge what needed
                game_board.merge(game_board.user_input, game_board.grid)

                #################################################################################

                # check for fake move:
                # 1. if past grid is the same as the move after the canges (True), we don't spown new number
                if game_board.check_unvilid_move(game_board.user_input):
                    print("No space for this move... try another direction")
                    invalidMove = True
                else: #2. past grid is diffrent as current grid -> correct! spown new number
                    # spown new number (2 or 4) in the grid
                    game_board.spown_new(game_board.grid, game_board.empty_cells)

                #################################################################################

            else: # user want to undo and go back to previous move
                print('Move delition...')  # user pressed 'u'
                game_board.undo()

            #####################################################################################

            # calculate the empty cells
            game_board.empty_cells = game_board.initialize_empty_coordinates(game_board.grid) # find cells with value 0

            #####################################################################################

            # pause the loop
            time.sleep(0.5)
            print('----------------') # separation from a grid to the other

        #####################################################################################

        # Prnt last grid
        game_board.update(game_board.grid) # print the grid that make u lose :)

#####################################################################################






'''
game_board = GameBoard(4)
GAME(game_board, 5)
'''