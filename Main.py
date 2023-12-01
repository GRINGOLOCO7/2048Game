import sys
sys.path.append('2048Game')
from colorama import Fore, Style
from utilities.game_class import GameBoard
from utilities.main_loop import GAME

def main():
    # initialize array
    print(f"\n\n\n\n\n{Fore.BLUE}{Style.BRIGHT}ROLES OF THE GAME:{Style.RESET_ALL}\n1. Move tiles with arrows\n2. press 'u' to undo, it will go back to previous move\n3. Press 'r' to show the ranking\n4. Arrive to 2048 with one tile to win\n5. fill all the spaces to lose")
    print(F"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Let's play!!{Style.RESET_ALL}")
    levels_for_tree_suggestion = int(input(f"{Fore.LIGHTYELLOW_EX}How deep do you want the tree to go? Do not exagerate with the depth ;)\nKeep it under 7 or your gameplay will be really slow\n(also it depend on the powe of your comuter but keep in mind that our tree has 4 child for node.. IT IS EXPONENTAL){Style.RESET_ALL}\t"))
    game_board = GameBoard(4)
    GAME(game_board, levels_for_tree_suggestion)



if __name__ == "__main__":
    main()