class Node:
    def __init__(self, value, next, score):  # self is the instance of this class
        self.value = value
        self.next = next
        self.score = score

 
class Stack:
    def __init__(self):
        self.top = None
        self.score = 0

    def push(self, value, score):
        node = Node(value, self.top, score)
        self.top = node
        self.top.score = score
        self.score = score

    def pop(self):
        if not self.top:
            return
        value= self.top
        self.top = self.top.next
        
        return value.value, value.score



#stack.pop() #--> 4
#print(stack.pop()) #--> 3
#stack.pop() #--> nothing
