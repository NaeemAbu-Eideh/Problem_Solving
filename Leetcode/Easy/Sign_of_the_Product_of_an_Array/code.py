class Solution(object):
    def arraySign(self, nums):
        length = len(nums)
        mult = 1
        for i in range(length):
            mult *= nums[i]
        if(mult > 0):
            return 1
        elif mult == 0:
            return 0
        else:
            return -1
        