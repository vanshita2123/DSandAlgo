'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        i = 0
        temp = self.head
        if index >= self.length:
            self.append(data)
            return
        if index == 0:
            self.prepend(data)
            return
        while i < self.length:
            if i == index - 1:
                temp.next, new_node.next = new_node, temp.next
                self.length += 1
                break
            temp = temp.next
            i += 1

    def remove(self, index):
        temp = self.head
        i = 0
        if index >= self.length:
            print("Entered wrong index")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        while i < self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            i += 1
            temp = temp.next

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data, end='')
            temp = temp.next
        print()
        print('Length=' + str(self.length))'''

'''
    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
            self.head = temp'''
'''

l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2, 99)
l.insert(34, 23)
l.remove(5)
#l.reverse()
l.printl()
print(l.head.data, l.tail.data)
'''
# Doubly linked lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length+=1
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length+=1
    def insert(self,index,data):
        new_node = Node(data)
        if index==0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        else:
            leader = self.traversetoindex(index - 1)
            holder = leader.next
            leader.next = new_node
            new_node.next = holder
            new_node.prev = leader
            holder.prev = new_node
            self.length+=1
    def remove(self,index):
        if index==0:
            self.head = self.head.next
            self.length-=1
            return
        leader = self.traversetoindex(index-1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.prev = leader
        self.length-=1
    def traversetoindex(self,index):
        curr_node = self.head
        i=0
        while i!=index:
            curr_node = curr_node.next
            i+=1
        return  curr_node
    def printt(self):
        temp = self.head
        while temp!=None:
            print(temp.data, end = ' ')
            temp = temp.next
        print()
        print('Length ' +str(self.length))

d = DoublyLinkedList()
d.append(10)
d.printt()

