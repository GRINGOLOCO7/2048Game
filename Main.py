import sys
sys.path.append('2048Game')
from colorama import Fore, Style
from utilities.game_class import GameBoard
from utilities.main_loop import GAME

def main():
    # initialize array
    print(f"{Fore.BLUE}{Style.BRIGHT}ROLES OF THE GAME:{Style.RESET_ALL}\n1. Move tiles with arrows\n2. press 'u' to undo, it will go back to previous move\n3. Arrive to 2048 with one tile to win\n4. fill all the spaces to lose")
    print(F"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Let's play!!{Style.RESET_ALL}")
    game_board = GameBoard(4)
    GAME(game_board)



if __name__ == "__main__":
    main()