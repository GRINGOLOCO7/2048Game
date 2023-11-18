class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.level = 0
        self.parent = None
        self.direction = None

    def insert_node(self, value, dir):
        new_node = TreeNode(value)
        new_node.level = self.level + 1
        new_node.parent = self
        new_node.direction = dir
        self.children.append(new_node)
        return new_node

def pretty_print(node, level=0):
    if not node:
        return

    spaces = ' ' * 4 * level
    print(f'{spaces} -> {node.value}')

    for child in node.children:
        pretty_print(child, level + 1)

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