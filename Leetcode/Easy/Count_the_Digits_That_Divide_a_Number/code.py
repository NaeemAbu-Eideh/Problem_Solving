class Solution:
    def countDigits(self, num: int) -> int:
        num2 = num
        count = 0
        while(num2 != 0):
            digit = num2 % 10
            if (num % digit == 0):
                count+=1
            num2 = num2 // 10
        return count