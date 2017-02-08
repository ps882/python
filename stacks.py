class Stacks:
    def __init__(self):
        self.max = 5
        self.head = 0
        self.stack = []

    def push(self,value):
        if not self.isfull():
            self.stack.insert(self.head,value)
            self.head += 1
            return True
        else:
            return False

    def pop(self):
        if not self.isempty():
            self.head -= 1
            return self.stack[self.head]
        else:
            return False

    def peek(self):
        return self.stack[self.head-1]

    def isempty(self):
        if self.head == 0:
            return True
        else:
            return False
    def isfull(self):
        if self.head >= self.max:
            return True
        else:
            return False

'''mystack = Stacks()
print mystack.push(4)
print mystack.push(5)
print mystack.push(1)
print mystack.peek()
print mystack.push(23)
print mystack.push(2)
print mystack.push(232)
print mystack.peek()
print mystack.pop()
print mystack.push(232)
print mystack.peek()'''
