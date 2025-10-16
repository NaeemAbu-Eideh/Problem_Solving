class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        result = start
        length = len(nums)
        for i in range(1, length):
            result = result ^ nums[i]
        return result