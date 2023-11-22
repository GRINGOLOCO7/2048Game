#from game_class import GameBoard           # comment this if u run main.py
from utilities.game_class import GameBoard  # comment this if u run current file
#from tree import TreeNode                  # comment this if u run main.py
from utilities.tree import TreeNode         # comment this if u run current file


class TreePossibilities:

    #####################################################################################

    def __init__(self, game_board):
        self.game_board = game_board

    #####################################################################################

    def spawn_number(self):
        self.game_board.spown_new()

    #####################################################################################

    def create_tree(self, depth):
        root = TreeNode(self.game_board.grid)
        directions = ['up', 'down', 'left', 'right']
        self.explore_tree(root, self.game_board, directions, depth)
        return root
    def explore_tree(self, node, grid, directions, depth):
        if depth == 0: # base case
            return
        self.spawn_number()
        for direction in directions:
            # Create a copy of the current grid to simulate the move
            temp_grid = [row[:] for row in grid.grid]
            # Create a copy of the game board for simulation
            temp_game_board = GameBoard(grid.size)
            temp_game_board.grid = temp_grid

            # Move & merge
            temp_game_board.move(direction)
            temp_game_board.merge(direction)

            # Save the resulting grid in the tree
            child = node.insert_node(temp_game_board.grid, direction)

            # Recursively explore the tree
            self.explore_tree(child, temp_game_board, directions, depth - 1)

    #####################################################################################

    def print_node_grid(self, child, direction, depth=0): # function that print on terminal the grid
        """
        Displays the given grid
        """
        spaces = '   ' * depth
        grid = child.value
        print(f'{spaces}-------{direction}-------')
        for row in grid: #pass trough each row
            # Use join to add spaces between elements in each row
            row_str = '   '.join([f'{num:5}' for num in row]) # this is to don't make the grid shif when big numbers arrive
            print(f"{spaces}{row_str}") #print each tiles number with the corrrect and adjusted space btw the others
        print(f'{spaces}---------------')
    def print_tree_grids(self, root, depth=0):
        """
        Recursively prints the grids in the tree.
        """
        if not root:
            return
        self.print_node_grid(root, root.direction, depth)
        for child in root.children:
            self.print_tree_grids(child, depth+1)

    #####################################################################################

    def find_nextGoal(self):
        '''
        method to check win condition
        '''
        max_value_in_grid = 2
        for row in range(len(self.game_board.grid)):
            for column in range(len(self.game_board.grid[row])):
                if self.game_board.grid[row][column] >  max_value_in_grid:
                    max_value_in_grid = self.game_board.grid[row][column]
        nextGoal = max_value_in_grid + max_value_in_grid
        return nextGoal
    def nextGoalReached(self):
        next_goal = self.find_nextGoal
        for row in range(len(self.game_board.grid)):
            for column in range(len(self.game_board.grid[row])):
                if self.game_board.grid[row][column] ==  next_goal:
                    return True
        return False

#####################################################################################





'''
# create board
game_board = GameBoard(4)  # is a grid -> is my grid
#create tree
tree_of_possibilities = TreePossibilities(game_board)
tree_of_possibilities.spawn_number()
tree_of_possibilities.spawn_number()
tree_of_possibilities.game_board.update()
print("\n\n")
root = tree_of_possibilities.create_tree(depth=2)
tree_of_possibilities.print_tree_grids(root)
print("\n\n")
print(tree_of_possibilities.game_board.grid)
print(tree_of_possibilities.find_nextGoal())
'''


