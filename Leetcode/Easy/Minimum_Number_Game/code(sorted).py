class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums2 = []
        length = len(nums)
        nums = sorted(nums)
        i = 0
        while(length > 0):
            min1 = nums[i]
            min2 = nums[i+1]
            nums2.append(min2)
            nums2.append(min1)
            length -= 2
            i += 2
        return nums2


        