class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            div = i * 10
            num = n // div
            num2 = num * i
            count += num2 + min(max( n%div -i + 1, 0), i)
            i *= 10
        return count
