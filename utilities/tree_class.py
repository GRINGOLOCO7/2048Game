from game_class import GameBoard           # comment this if u run main.py
#from utilities.game_class import GameBoard  # comment this if u run current file
from tree import TreeNode                  # comment this if u run main.py
#from utilities.tree import TreeNode         # comment this if u run current file



class TreePossibilities:
    def __init__(self, grid): # recive a grid and will create the tree of possibilities
        copied_grid = [row[:] for row in grid] # make a copy of the grid to avoid comunications with gameboard grid
        self.size = len(grid) # calculate size grid
        self.board_game = GameBoard(self.size) # create a istance from the class game board
        self.board_game.grid = copied_grid
        self.board_game.empty_cells = self.board_game.initialize_empty_coordinates(self.board_game.grid)
        self.board_game.spown_new(self.board_game.grid, self.board_game.empty_cells)
        self.board_game.grid = copied_grid

    def create_tree(self, depth):
        root = TreeNode(self.board_game.grid, self.board_game.score)
        directions = ['up', 'down', 'left', 'right']
        self.explore_tree(root, directions, depth)
        self.print_tree_grids(root)
        return root
    def explore_tree(self, node, directions, depth):
        if depth == 0:  # base case
            return

        #print(f"Directrion: {node.direction}\nDeph: {depth}\nGrid: {node.value}\n")
        for direction in directions:
            temporary_node = TreePossibilities(node.value)
            #print(temporary_node.board_game.grid)
            temporary_node.board_game.move(direction, temporary_node.board_game.grid)
            temporary_node.board_game.merge(direction, temporary_node.board_game.grid)
            score = temporary_node.board_game.score + node.score
            child = node.insert_node(temporary_node.board_game.grid, score, direction)
            self.explore_tree(child, directions, depth-1)

    def print_node_grid(self, child, direction, depth=0):
        spaces = '      ' * depth
        grid = child.value
        print(f'{spaces}-------{direction}--{child.score}-------')
        for row in grid: #pass trough each row
            # Use join to add spaces between elements in each row
            row_str = '   '.join([f'{num:5}' for num in row]) # this is to don't make the grid shif when big numbers arrive
            print(f"{spaces}{row_str}") #print each tiles number with the corrrect and adjusted space btw the others
        print(f'{spaces}--------------------')
    def print_tree_grids(self, node, depth=0):
        """
        Recursively prints the grids in the tree.
        """
        if not node:
            return
        self.print_node_grid(node, node.direction, depth)
        for child in node.children:
            self.print_tree_grids(child, depth+1)

    #TRAVERSE TREE AND FIND HIGHER SCORE
    #USE THE DIRECTIONS TO ADVICE THE USER (approximation of where the higher score will be)
    #SAVE THE DIRECTION TO CHOSE FROM THE ROOT
    #IN MAIN LOOP RECALCULATE EACH TIME THE TREE AND TH EDIRECTIONS
game_board = GameBoard(4)
root = TreePossibilities(game_board.grid)
print(f"Size: {root.size}\nTreeGrid: {root.board_game.grid}\nGameGrid: {game_board.grid}")
root.create_tree(5)
