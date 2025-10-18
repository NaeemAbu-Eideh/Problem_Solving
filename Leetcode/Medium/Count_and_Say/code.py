class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(1, n):
            current = result
            result = ''
            count = 1

            length = len(current)
            for j in range(1, length):
                if current[j] == current[j-1]:
                    count += 1
                else:
                    result += str(count) + current[j-1]
                    count = 1
            result += str(count) + current[-1]
        return result