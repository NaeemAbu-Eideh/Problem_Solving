class MinStack(object):

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val):
        self.st.append(val)
        if not self.minSt or val <= self.minSt[-1]:
            self.minSt.append(val)

    def pop(self):
        val = self.st.pop()
        if val == self.minSt[-1]:
            self.minSt.pop()

    def top(self):
        return self.st[-1]

    def getMin(self):
        return self.minSt[-1]