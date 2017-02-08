class Node:
    def __init__(self,value):
        self.root = value
        self.right = None
        self.left = None

    def get_value(self):
        return self.root

    def set_value(self , value):
        self.root = value
        return True

    def get_right(self):
        return self.right

    def set_right(self, value):
        self.right = value
        return True

    def get_left(self):
        return self.left

    def set_left(self, value):
        self.left = value
        return True

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        new = Node(value)
        self.size += 1
        if self.root :
            spointer = self.root
            spointer_p = None
            while spointer:
                #print value , spointer.get_value() , " are values"
                if value < spointer.get_value():
                    spointer_p = spointer
                    spointer = spointer.get_left()
                elif value > spointer.get_value():
                    spointer_p = spointer
                    spointer = spointer.get_right()
                else:
                    self.size -= 1
                    return False
            if value < spointer_p.get_value():
                spointer_p.set_left(new)
                return True
            else:
                spointer_p.set_right(new)
                return True
        else:
            self.root = new
            return True
        #print "done"

    def find(self, value):
        pointer = self.root
        while pointer:
            if pointer.get_value() == value:
                return True
            elif pointer.get_value() > value:
                pointer = pointer.get_left()
            else:
                pointer = pointer.get_right()
        return False

    def preorder(self, head):
        if head :
            print head.get_value()
            self.preorder(head.get_left())
            self.preorder(head.get_right())

    def inorder(self, head):
        if head:
            self.inorder(head.get_left())
            print head.get_value()
            self.inorder(head.get_right())


    def postorder(self, head):
        if head:
            self.postorder(head.get_left())
            self.postorder(head.get_right())
            print head.get_value()

    def ipreorder(self):
        mystack = [self.root]
        while len(mystack) > 0:
            popped = mystack.pop()
            print popped.get_value()
            if popped.get_right() is not None:
                mystack.append(popped.get_right())
            if popped.get_left() is not None:
                mystack.append(popped.get_left())

    def iinorder(self):
        mystack = [self.root]
        head = self.root
        while len(mystack) > 0:
            if head is not None:
                if head.get_left() is not None:
                    mystack.append(head.get_left())
                head = head.get_left()
            else:
                popped = mystack.pop()
                print popped.get_value()
                if popped.get_right() is not None:
                    mystack.append(popped.get_right())
                head = popped.get_right()

    def ipostorder(self):
        mystack = [self.root]
        finstack = []
        head = self.root
        while len(mystack) > 0:
            popped = mystack.pop()
            #print popped.get_value()
            finstack.append(popped)
            if popped.get_left() is not None:
                mystack.append(popped.get_left())
            if popped.get_right() is not None:
                mystack.append(popped.get_right())
        while len(finstack) > 0:
            print finstack.pop().get_value()


    def remove(self, value):
        #print "root and deletion value are " , self.root.get_value() , value
        if self.root == None:
            return False

        if self.root.get_value() == value:
            self.size -= 1
            if self.root.get_left() == None:
                if self.root.get_right() == None:
                    self.root = None
                    return True
                else:
                    self.root = self.root.get_right()
                    return True
            elif self.root.get_right() == None:
                self.root = self.root.get_left()
                return True
            else:
                delnode , pdelnode = self.get_leftmost(self.root.get_right(),self.root)
                #print delnode.get_value() , pdelnode.get_value()
                if delnode.get_value() > pdelnode.get_value():
                    print "j"
                    pdelnode.set_right(delnode.get_right())
                    self.root.set_value(delnode.get_value())
                    return True
                else:
                    pdelnode.set_left(delnode.get_right())
                    self.root.set_value(delnode.get_value())
                    return True

        pointer = self.root
        p_pointer = None
        while pointer and pointer.get_value() != value:
            if pointer.get_value() < value:
                p_pointer = pointer
                pointer = pointer.get_right()
            else:
                p_pointer = pointer
                pointer = pointer.get_left()

        if pointer.get_value() != value or pointer is None:
            return False

        self.size -= 1
        if not pointer.get_left():
            if not pointer.get_right():
                if p_pointer.get_value() > pointer.get_value():
                    p_pointer.set_left(None)
                    return True
                else:
                    p_pointer.set_right(None)
                    return True
            else:
                if p_pointer.get_value() > pointer.get_value():
                    p_pointer.set_left(pointer.get_right())
                    return True
                else:
                    p_pointer.set_right(pointer.get_right())
                    return True
        else:
            if not pointer.get_right():
                if p_pointer.get_value() > pointer.get_value():
                    p_pointer.set_left(pointer.get_left())
                    return True
                else:
                    p_pointer.set_right(pointer.get_left())
                    return True
            else:
                #print pointer.get_value() , p_pointer.get_value()
                delnode , pdelnode = self.get_leftmost(pointer.get_right() , pointer)
                #print delnode.get_value() , pdelnode.get_value()
                if delnode.get_value() > pdelnode.get_value():
                    pdelnode.set_right(delnode.get_right())
                    pointer.set_value(delnode.get_value())
                    return True
                else:
                    pdelnode.set_left(delnode.get_right())
                    pointer.set_value(delnode.get_value())
                    return True

    def get_leftmost(self, node, pnode):
        pointer = node
        p_pointer = pnode
        while pointer.get_left():
            p_pointer = pointer
            pointer = pointer.get_left()
        return pointer , p_pointer

    def compare_tree(self, nodea , nodeb):
        if nodea is None and nodeb is None:
            return True
        if nodea is None or nodeb is None:
            return False
        if nodea.get_value() != nodeb.get_value():
            return False
        else:
            return self.compare_tree(nodea.get_left(), nodeb.get_left()) and self.compare_tree(nodea.get_right(),nodeb.get_right())

    def get_height(self,node):
        if node is None:
            return 0
        else:
            height = max(self.get_height(node.get_right()), self.get_height(node.get_left()))
        return height + 1

    def isbinary(self, node, amin, amax):
        if node is None:
            return True
        elif node.get_value() < amax and node.get_value > amin:
            minr = max(amin, node.get_value())
            minl = amin
            maxr = amax
            maxl = min(amax, node.get_value())
            return self.isbinary(node.get_right(), minr, maxr) and self.isbinary(node.get_left(), minl, maxl)
        else:
            return False

mybst = BST()
mybst.add(5)
mybst.add(53)
mybst.add(15)
mybst.add(115)
mybst.add(151)
#print mybst.root.get_value()
#mybst.preorder(mybst.root)
#mybst.inorder(mybst.root)
#mybst.postorder(mybst.root)
#print "find"
#print mybst.find(4)
#print mybst.find(53)
#print "removing 53"
#print mybst.remove(5)
#mybst.inorder(mybst.root)
#print mybst.remove(53)
#print mybst.remove(151)
#print mybst.remove(15)
#print mybst.remove(5)
#mybst.inorder(mybst.root)
mybst2 = BST()
mybst2.add(5)
mybst2.add(53)
mybst2.add(15)
mybst2.add(115)
mybst2.add(151)
mybst2.add(1)
#mybst2.add(12)
#print mybst.compare_tree(mybst.root, mybst2.root)
#print mybst.size
#print mybst2.get_height(mybst2.root)
#print mybst.isbinary(mybst.root, -99999999 , 999999999)
#mybst2.ipreorder()
#mybst2.iinorder()
mybst2.ipostorder()