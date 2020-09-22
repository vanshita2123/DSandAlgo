class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.val < temp.val:
                if temp.left == None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            elif new_node.val > temp.val:
                if temp.right == None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right
                    