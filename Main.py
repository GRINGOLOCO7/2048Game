from utilities.game_class import GameBoard


def main():
    # initialize array
    print("ROLES OF THE GAME:\n1. Move tiles with arrows\n2. press 'u' to undo, it will go back to previous move\n3. Arrive to 2048 with one tile to win\n4. fill all the spaces to lose")
    print("Let's play... But first:")
    print("Chose the size of your grid\nHow much do you want ot challeng your-self?\n(Usually the grid is a 4x4)")
    size = int(input("So... what is the size of the grid:\t"))
    game_board = GameBoard(size)
    game_board.GAME()



if __name__ == "__main__":
    main()