class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        minus_num = 0
        if(num == 0):
            return "0"
        if(num < 0):
            minus_num = num
            num += -2*num
        while(num != 0):
            result = str(num % 7) + result
            num = int(num / 7)
        if(minus_num != 0):
            result = "-" + result
        return result