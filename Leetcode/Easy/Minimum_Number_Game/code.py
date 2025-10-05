class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums2 = []
        length = len(nums)
        while(length > 0):
            min1 = nums[0]
            index1 = 0
            for i in range(length):
                if(min1 > nums[i]):
                    min1 = nums[i]
                    index1 = i
            nums.pop(index1)
            length -= 1
            min2 = nums[0]
            index2 = 0
            for i in range(length):
                if(min2 > nums[i]):
                    min2 = nums[i]
                    index2 = i
            nums.pop(index2)
            length -= 1
            nums2.append(min2)
            nums2.append(min1)
        return nums2
        