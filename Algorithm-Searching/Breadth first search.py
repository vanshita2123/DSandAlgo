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

    def breadthfirstsearch(self):
        curr_node = self.root
        mylist = []
        queue = []
        queue.append(curr_node)

        while len(queue)>0:
            curr_node = queue[0]
            del queue[0]
            mylist.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return mylist

    def recursivebfs(self, queue, mylist):
        if len(queue) == 0:
            return mylist
        curr_node = queue[0]
        del queue[0]
        mylist.append(curr_node.val)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

        return self.recursivebfs()

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

x = tree.lookup(170)
print(x)
print(tree.breadthfirstsearch())
print(tree.recursivebfs([tree.root],[]))