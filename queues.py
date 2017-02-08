class Queues:
    def __init__(self):
        self.head = 0
        self.max = 5
        self.queue = []

    def push(self,value):
        if not self.isfull():
            self.queue.insert(self.head,value)
            self.head += 1
            return True
        else:
            return False

    def pop(self):
        if not self.isempty():
            self.head -= 1
            return self.queue.pop(0)
        else:
            return False

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

    def peek(self):
        return self.queue[self.head-1]

'''queue = Queues()
print queue.push(4)
print queue.push(5)
print queue.push(1)
print queue.peek()
print queue.push(23)
print queue.push(2)
print queue.push(232)
print queue.peek()
print queue.pop()
print queue.push(232)
print queue.peek()'''

