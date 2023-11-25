import sys
sys.path.append('2048Game\\utilities')
from game_class import GameBoard           # comment this if u run main.py
from tree import TreeNode                  # comment this if u run main.py


class TreePossibilities:
    def __init__(self, grid): # recive a grid and will create the tree of possibilities
        copied_grid = [row[:] for row in grid] # make a copy of the grid to avoid comunications with gameboard grid
        self.size = len(grid) # calculate size grid
        self.board_game = GameBoard(self.size) # create a istance from the class game board
        self.board_game.grid = copied_grid # attach to the grid game the copied grid
        self.board_game.empty_cells = self.board_game.initialize_empty_coordinates(self.board_game.grid)  # find the empty celles using game_class method
        self.board_game.spown_new(self.board_game.grid, self.board_game.empty_cells) # spawn a number in our grid using game_class method
        self.board_game.grid = copied_grid # attach the updated to the grid game the copied grid

    def create_tree(self, depth): # method that create a tree with as much levels as depth. each node will have 4 childrens for the 4 possible directions
        root = TreeNode(self.board_game.grid, self.board_game.score) # create root using class TreeNode, where first argument is grid, second the score and third is the direction that for the root is equal none
        directions = ['up', 'right', 'left', 'down'] # initialize possible moves
        self.explore_tree(root, directions, depth) # create the childrens using this method


        #self.print_tree_grids(root) # function to print the tree -> comment this line


        return root # return head of the tree
    def explore_tree(self, node, directions, depth): # create the childrens of a given node
        if depth == 0:  # base case
            return

        #print(f"Directrion: {node.direction}\nDeph: {depth}\nGrid: {node.value}\n")
        for direction in directions: # for each direction create a child from the given node
            temporary_node = TreePossibilities(node.value) # create a istance of TreePossibilities class
            #print(temporary_node.board_game.grid)
            temporary_node.board_game.move(direction, temporary_node.board_game.grid) # move the new grid
            temporary_node.board_game.merge(direction, temporary_node.board_game.grid) # merge the possible move
            score = temporary_node.board_game.score + node.score # update the score of the current grid
            child = node.insert_node(temporary_node.board_game.grid, score, direction) # append the child to the node using insert_node method of class TreeNode, where where first argument is grid, second the score and third is the direction
            self.explore_tree(child, directions, depth-1) # recursively create all the others children for each node utill level reached

    def print_node_grid(self, child, direction, depth=0): # is a sort off preatty_print function we used in class for binary tree,
        spaces = '      ' * depth                         # the only difference is that each node has 4 children
        grid = child.value
        print(f'{spaces}-------{direction}--{child.score}-------')
        for row in grid: #pass trough each row
            # Use join to add spaces between elements in each row
            row_str = '   '.join([f'{num:5}' for num in row]) # this is to don't make the grid shif when big numbers arrive
            print(f"{spaces}{row_str}") #print each tiles number with the corrrect and adjusted space btw the others
        print(f'{spaces}--------------------')
    def print_tree_grids(self, node, depth=0): # use recurtion to print each node
        """
        Recursively prints the grids in the tree.
        """
        if not node:
            return
        self.print_node_grid(node, node.direction, depth)
        for child in node.children:
            self.print_tree_grids(child, depth+1)

    #TRAVERSE TREE AND FIND HIGHER SCORE (inorder)
    #USE THE DIRECTIONS TO ADVICE THE USER (approximation of where the higher score will be)
    #SAVE THE DIRECTION TO CHOSE FROM THE ROOT
    def higher_values(self, root): # method that return an array with 4 values. each one rappresent a direction from the root and the higer score
        max_val_in_each_direction = [float("-inf")] * 4 # create array with 4 spaces to store the maximum score in each branch from root
        directions = ['up', 'right', 'left', 'down'] # inotialize directions
        for idx_dir in range(len(directions)): # for each cildren from the root (up, down, left, right) find higer value in that path
            #print(root.children[idx_dir].direction)
            maximum = max_val_in_each_direction[idx_dir]
            max_score = self.traverse(root.children[idx_dir], maximum) # find max score in the branch with direction[idx_dir]
            max_val_in_each_direction[idx_dir] = (directions[idx_dir], max_score) # attach that score to the list
        return max_val_in_each_direction # return an array with 4 tuples
    #traverse the node and find higher score
    def traverse(self, node, maximum): # used for recursively traverse the node path and store the maximum score
        if not node:
            return maximum
        #print(f"dir: {node.direction}\ngrid: {node.value}")
        if node.score > maximum:
            maximum = node.score
        for child in node.children:
            maximum = self.traverse(child, maximum) # recursively go deep in this path and save maximum score founded
        return maximum
    #IN MAIN LOOP RECALCULATE EACH TIME THE TREE AND TH EDIRECTIONS

    def find_maxscore_in_direction(self, max_val_in_each_direction): # method that recive a array of tupples, find the max value and return the direction refeared to it... it will be the best direction to take from the root
        best = float('-inf') # set beast score to -inf
        advice = None # store the best direction to take from the root, based on the path with higher score
        for dir, score in max_val_in_each_direction:
            #print(f"Score: {score}\nDirection: {dir}\nBest: {best}\n")
            if score > best:
                best = score
                advice = dir
        return advice

'''
game_board = GameBoard(4)
tree = TreePossibilities(game_board.grid)
#print(f"Size: {root.size}\nTreeGrid: {root.board_game.grid}\nGameGrid: {game_board.grid}")
root = tree.create_tree(3)
listOFadvice = tree.higher_values(root)
print(listOFadvice)
advice = tree.find_maxscore_in_direction(listOFadvice)
print(advice)
'''