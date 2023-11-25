class TreeNode:
    def __init__(self, value, score, direction=None):
        self.value = value
        self.direction = direction
        self.score = score
        self.children = []

    def insert_node(self, value, score, direction):
        new_node = TreeNode(value, score, direction)
        self.children.append(new_node)
        return new_node

#####################################################################################






'''
# Example usage:
root = TreeNode(1)

child1 = root.insert_node(2)
child2 = root.insert_node(3)
child3 = root.insert_node(4)
child4 = root.insert_node(5)

child1_1 = child1.insert_node(4)
child1_2 = child1.insert_node(4)
child1_3 = child1.insert_node(4)
child1_4 = child1.insert_node(4)

child2_1 = child2.insert_node(6)
child2_2 = child2.insert_node(6)
child2_3 = child2.insert_node(6)

#pretty_print(root)

 -> 1
     -> 2
         -> 4
         -> 4
         -> 4
         -> 4
     -> 3
         -> 6
         -> 6
         -> 6
     -> 4
     -> 5
'''