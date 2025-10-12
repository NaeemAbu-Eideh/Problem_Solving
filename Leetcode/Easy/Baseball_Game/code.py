class Solution:
    def calPoints(self, operations: List[str]) -> int:
        num = []
        for i in operations:
            if i == 'C':
                num.pop()
            elif i == 'D':
                num.append(num[-1] * 2)
            elif i == '+':
                num.append(num[-1] + num[-2])
            else:
                num.append(int(i))  
        return sum(num)