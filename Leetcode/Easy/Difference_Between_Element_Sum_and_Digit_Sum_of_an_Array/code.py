class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for i in nums:
            element_sum += i
            num = i
            while(num != 0):
                digit_sum += (num%10)
                num = num // 10
        return element_sum - digit_sum