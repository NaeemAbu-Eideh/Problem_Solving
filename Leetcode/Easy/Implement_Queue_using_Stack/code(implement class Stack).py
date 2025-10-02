class Stack:
    def __init__(self):
        self.stack = []
    
    def pushStack(self,val):
        self.stack.append(val)
    
    def popStack(self):
        self.stack.pop()
    
    def topStack(self):
        return self.stack[-1] 
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def length(self):
        return len(self.stack)


class MyQueue(object):

    def __init__(self):
        self.stack = Stack()

    def push(self, x):
        self.stack.pushStack(x)

    def pop(self):
        stack2 = Stack()
        while( self.stack.length() != 1):
            stack2.pushStack(self.stack.topStack())
            self.stack.popStack()
        val = self.stack.topStack()
        self.stack.popStack()
        while(not stack2.is_empty()):
            self.stack.pushStack(stack2.topStack())
            stack2.popStack()
        return val


    def peek(self):
        stack2 = Stack()
        while( self.stack.length() != 1):
            stack2.pushStack(self.stack.topStack())
            self.stack.popStack()
        val = self.stack.topStack()
        stack2.pushStack(self.stack.topStack())
        self.stack.popStack()
        while(not stack2.is_empty()):
            self.stack.pushStack(stack2.topStack())
            stack2.popStack()
        return val
        

    def empty(self):
        if(self.stack.is_empty()):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()