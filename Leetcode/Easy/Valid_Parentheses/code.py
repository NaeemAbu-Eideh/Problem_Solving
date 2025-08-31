class Solution(object):
    def isValid(self, s):
        stack = []
        dec = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in dec.values(): 
                stack.append(i)
            elif i in dec: 
                if not stack or stack[-1] != dec[i]:
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0                