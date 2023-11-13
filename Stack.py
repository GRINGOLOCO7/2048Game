class Node:
    def __init__(self, value, score, next):  # Add score parameter
        self.value = value
        self.score = score
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value, score):  # Add score parameter
        node = Node(value, score, self.top)
        self.top = node

    def pop(self):
        if not self.top:
            return None, None  # Return a tuple of None values
        value = self.top.value
        score = self.top.score
        self.top = self.top.next
        return value, score  # Return a tuple of value and score

stack = Stack()
stack.push(3)
stack.push(4)
#stack.pop() #--> 4
#print(stack.pop()) #--> 3
#stack.pop() #--> nothing