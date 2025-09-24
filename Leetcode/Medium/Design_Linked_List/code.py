class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if(self.size == 0 or index < 0 or index >= self.size):
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if(self.size == 0):
            self.head = node
            self.tail = node
            self.size += 1
            return
        node.next = self.head
        self.head = node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if(self.size == 0):
            self.head = node
            self.tail = node
            self.size += 1
            return
        self.tail.next = node
        self.tail = node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if (index == 0):
            self.addAtHead(val)
            return
        
        if(index > 0 and index < self.size):
            node = Node(val)
            current = self.head
            for i in range(index-1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1    
        if(index == self.size):
            self.addAtTail(val)
            return
        else:
            return -1
        

    def deleteAtIndex(self, index: int) -> None:
        if(self.size == 0 or index > self.size or index < 0):
            return -1
        if(index == 0 and self.size == 0):
            self.head = None
            self.tail = None
            self.size -= 1
            return
        if(index == 0 and self.size != 0):
            self.head = self.head.next
            self.size -= 1
            return
        
        if(index > 0 and index < self.size):
            current = self.head.next
            prev = self.head
            for i in range(1,index):
                prev = current
                current = current.next
            if(current.next == None):
                self.tail = prev
            prev.next = current.next
            self.size -= 1
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)