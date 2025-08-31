class Solution(object):
    def intersection(self, nums1, nums2):
        num1 = set(nums1)
        num2 = set(nums2)
        return list(num1 & num2)
        