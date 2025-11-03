class Solution:
    def reverse(self, x: int) -> int:


        rev_str = ""
        if x < 0:
            rev_str += '-'
            x = -x
        rev_str2 = ""
        num = str(x)
        length = len(num)
        for i in range(length-1, -1, -1):
            rev_str2 += num[i]
        rev_str += rev_str2
        x = int(rev_str)
        if x > 2147483647 or x < -2147483648:
            return 0 
        return x