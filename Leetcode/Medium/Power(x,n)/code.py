class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {0: 1, 1: x}
        def memo_rec(num , power):
            if power in memo:
                return memo[power]
            if(power % 2 == 1):
                power = power-1
                memo[power] = memo_rec(num, power/2) * memo_rec(num, power/2)
                memo[power+1] = memo[power] * num
                power = power + 1
                return memo[power]
            memo[power] = memo_rec(num, power/2) * memo_rec(num, power/2)
            return memo[power]
        
        number = 0
        if(n < 0):
            n = -2 * n + n
            number = memo_rec(x, n)
            return 1/ number
        return memo_rec(x, n)