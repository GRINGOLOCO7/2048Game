class Node:
    def __init__(self, value, next):  # self is the instance of this class
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value, self.top)
        self.top = node

    def pop(self):
        if not self.top:
            return
        value = self.top.value
        self.top = self.top.next
        return value


stack = Stack()
stack.push(3)
stack.push(4)
stack.pop() #--> 4
print(stack.pop()) #--> 3
stack.pop() #--> nothing