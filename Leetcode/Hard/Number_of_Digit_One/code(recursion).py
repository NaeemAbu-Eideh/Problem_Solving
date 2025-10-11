class Solution:
    def countDigitOne(self, n: int) -> int:
        def rec(num, i):
            if(i > num):
                return 0
            div = i * 10
            number1 = n//div
            number1 = number1 * i
            number1 = number1 + min(max( n%div -i + 1, 0), i)
            return  number1 + rec(num, i*10)
        return rec(n, 1)
