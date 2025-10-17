class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for item in accounts:
            sum = 0
            for i in item:
                sum += i
            if max < sum:
                max = sum
        return max