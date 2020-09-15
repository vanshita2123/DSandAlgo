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
                temp.next = new_node
                new_node.next = temp.next
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

# When given reference to head node,
    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data, end='')
            temp = temp.next
        print()
        print('Length=' + str(self.length))

# To get the value at a given index
    def getNth(head, k):
        temp = head
        i = 0
        while (temp):
            if (i == k - 1):
                return temp.data
            i += 1
            temp = temp.next

# To find the data at the middle index of the linked list
    def findMid(head):
        temp = head
        count = 0
        i = 0
        while (temp):
            count += 1
            temp = temp.next
        if (count % 2 == 0):
            temp = head
            while (temp):
                if (i == count / 2):
                    return temp.data
                temp = temp.next
                i += 1
        if (count % 2 != 0):
            temp = head
            while (temp):
                if (i == count // 2):
                    return temp.data
                temp = temp.next
                i += 1
# function inserts data x in front of list and returns new head
    def insertAtBegining(head,x):
        new_node = Node(x)
        if head == None:
            head = new_node
        else:
            new_node.next = head
            head = new_node
        return head

# function appends data x at the end of list and returns new head
    def insertAtEnd(head,x):
        new_node = Node(x)
        if head == None:
            head = new_node
        else:
            ptr = head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
        return head


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
