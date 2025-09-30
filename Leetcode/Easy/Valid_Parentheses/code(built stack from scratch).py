class Solution(object):
    def __init__(self):
        self.stack = []
        self.dec = {')':'(', ']':'[', '}':'{'}
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def is_empty(self, stack):
        if(len(stack) == 0):
            return True
        return False
    def langth(self):
        return len(self.stack)
    
    def isValid(self, s):
        for i in s:
            if i in self.dec.values(): 
                self.push(i)
            elif i in self.dec: 
                if self.is_empty(self.stack) or self.top() != self.dec[i]:
                     return False
                self.pop()
            else:
                 return False
        return self.is_empty(self.stack)         