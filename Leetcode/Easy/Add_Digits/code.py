class Solution:
    def addDigits(self, num: int) -> int:
        string = str(num)
        length = len(string)
        while(length != 1):
            sum = 0
            for char in string:
                sum += int(char)
            string = str(sum)
            length = len(string)
        return int(string)