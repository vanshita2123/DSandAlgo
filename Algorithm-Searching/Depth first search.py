class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySeacrhTree:
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

    def lookup(self, val):
        temp = self.root
        while True:
            if temp.val == val:
                return True
            elif temp == None:
                return False
            elif val < temp.val:
                temp = temp.left
            elif val > temp.val:
                temp = temp.right

    def inorder(self, curr_node, mylist):
        if curr_node != None:
            self.inorder(curr_node.left, mylist)
            mylist.append(curr_node.val)
            self.inorder(curr_node.right, mylist)
        return mylist

    def preorder(self, curr_node, mylist):
        if curr_node != None:
            mylist.append(curr_node.val)
            self.preorder(curr_node.left, mylist)
            self.preorder(curr_node.right, mylist)
        return mylist

    def postorder(self, curr_node, mylist):
        if curr_node.left:
            self.postorder(curr_node.left, mylist)
        if curr_node.right:
            self.postorder(curr_node.right, mylist)
        mylist.append(curr_node.val)
        return mylist

tree = BinarySeacrhTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.inorder(tree.root, []))
print(tree.preorder(tree.root, []))
print(tree.postorder(tree.root, []))

