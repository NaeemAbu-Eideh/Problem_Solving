class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice = 0
        bob = 0
        length = len(nums)
        for i in range(length):
            if(nums[i] >= 0 and nums[i] <= 9):
                alice += nums[i]
            else:
                bob += nums[i]
        if(alice != bob):
            return True
        return False
        