class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        str_num = ""
        length = len(s)
        for i in range(length):
            if(i == 0 and (s[i] == '-' or s[i] == '+' )):
                str_num += s[i]
                
            else:
                if s[i] >= '0' and s[i] <= '9':
                    str_num += s[i]
                else:
                    break
        if(len(str_num) == 0 or str_num == '-' or str_num == '+'):
            str_num = "0"
        number = int(str_num)

        if number >= 2147483647:
            return 2147483647
        if number <= -2147483648:
            return -2147483648
        if(len(str_num)) == 0:
            return 0
        return int(str_num)