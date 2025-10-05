class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums2 = []
        length = len(nums)
        while(len(nums) > 0):
            min1 = min(nums)
            nums.remove(min1)
            min2 = min(nums)
            nums.remove(min2)
            nums2.append(min2)
            nums2.append(min1)
        return nums2


        