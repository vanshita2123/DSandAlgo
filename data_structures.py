

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
        print('Length=' + str(self.length))

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
d.append(5)
d.append(6)
d.prepend(1)
d.insert(2,22)
d.remove(3)
d.printt()

# Stacks
# Stacks using linked lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self,data):
        new_node = Node(data)
        if self.bottom == None:
            self.bottom = new_node
            self.top = new_node
            self.top = self.bottom
            self.length = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length+=1

    def pop(self):
        if not self.top:
            return None
        holderPointer = self.top
        self.top=self.top.next
        self.length-=1
        if self.length==0:
            self.bottom = None
        return holderPointer.data

    def printt(self):
        temp = self.top
        while temp!=None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print()

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.printt()
x = mystack.peek()
print(x)
y = mystack.pop()
print(y)
mystack.printt()
qw = mystack.peek()
print(qw)

# Stacks using arrays
class Stack:
    def __init__(self):
        self.arr = []
        self.length = 0

    def peek(self):
        return self.arr[self.length-1]

    def push(self,value):
        self.arr.append(value)
        self.length+=1

    def pop(self):
        popped_item = self.arr[self.length-1]
        del self.arr[self.length-1]
        self.length-=1
        return popped_item

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
print(mystack)
x = mystack.peek()
print(x)
mystack.pop()
print(mystack)

# Queue using linked lists
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.val

    def enqueue(self,val):
        new_node = Node(val)
        if self.first == None:
            self.first = new_node
            self.last = self.first
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length+=1

    def dequeue(self):
        temp = self.first.next
        dequeued_element = self.first
        if temp == None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = temp
        self.length -= 1

    def printt(self):
        temp = self.first
        while temp != None:
            print(temp.val, end=' --> ')
            temp = temp.next
        print()
        print(self.length)

myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.printt()
myq.dequeue()
myq.printt()
x = myq.peek()
print(x)


