class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        sum = 0
        mult = 1
        for i in string:
            sum += int(i)
            mult *= int(i)
        return mult - sum
