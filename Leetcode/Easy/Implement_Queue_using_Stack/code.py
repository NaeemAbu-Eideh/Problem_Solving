class MyQueue(object):


    
    def __init__(self):
        self.inStack = []
        self.outStack = []


    def transferIfNeeded(self):
        if len(self.outStack) == 0:
            while self.inStack:
                self.outStack.append(self.inStack.pop())


    def push(self, x):
        self.inStack.append(x)
        

    def pop(self):
        self.transferIfNeeded()
        val = self.outStack[-1]
        self.outStack.pop()
        return val

        

    def peek(self):
        self.transferIfNeeded()
        return self.outStack[-1]
        

    def empty(self):
        return not self.inStack and not self.outStack