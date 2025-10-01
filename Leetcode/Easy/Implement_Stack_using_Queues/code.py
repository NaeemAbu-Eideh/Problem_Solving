class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)
    
class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)

    def pop(self) -> int:
        queue1 = Queue()
        while(self.queue.length() != 1):
            queue1.enqueue(self.queue.front())
            self.queue.dequeue()
        val = self.queue.front()
        self.queue.dequeue()
        self.queue = queue1
        return val

    def top(self) -> int:
        queue1 = Queue()
        while(self.queue.length() != 1):
            queue1.enqueue(self.queue.front())
            self.queue.dequeue()
        val = self.queue.front()
        queue1.enqueue(self.queue.front())
        self.queue.dequeue()
        self.queue = queue1
        return val

    def empty(self) -> bool:
        return self.queue.length() == 0
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()