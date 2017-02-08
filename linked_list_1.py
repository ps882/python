class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_next(self):
        return self.next
    def get_data(self):
        return self.data
    def set_next(self, next):
        self.next = next
    def set_data(self, data):
        self.data = data

class LinkedList():
    def __init__(self):
        self.root = None
        self.size = 0
    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.root)
        self.root = new_node
        self.size += 1
    def print_all(self):
        pointer = self.root
        while pointer:
            print pointer.get_data()
            pointer = pointer.get_next()
    def find(self,data):
        pointer = self.root
        while pointer:
            if pointer.get_data() == data:
                return True
            else:
                pointer = pointer.get_next()
        return False
    def remove(self,data):
        pointer = self.root
        previous = None
        while pointer:
            if pointer.get_data() == data:
                if previous == None:
                    self.root = pointer.get_next()
                else:
                    previous.set_next(pointer.get_next())
                self.size -= 1
                return True
            else:
                previous = pointer
                pointer = pointer.get_next()
        return False


ll = LinkedList()
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)
ll.print_all()
print ll.find(5)
print ll.find(10)
print ll.remove(56)
print ll.remove(5)
ll.print_all()