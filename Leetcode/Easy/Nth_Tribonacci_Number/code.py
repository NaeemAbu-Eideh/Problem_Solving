class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        def memo_rec(n):
            if n in memo:
                return memo[n]
            memo[n] = memo_rec(n-1) + memo_rec(n-2) + memo_rec(n-3)
            return memo[n]
        result = memo_rec(n)
        print(result)
        return memo_rec(n)