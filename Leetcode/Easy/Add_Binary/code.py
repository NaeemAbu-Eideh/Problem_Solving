class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        if(len_a > len_b):
            for i in range(len_b, len_a):
                b = "0" + b
            len_b = len(b)
        elif(len_b > len_a):
            for i in range(len_a, len_b):
                a = "0" + a
            len_a = len(a)
        carry = 0
        result = ""
        print(f"a: {a}, b: {b}")
        for i in range(len_a-1, -1, -1):
            if(a[i] == '0' and b[i] == "0"):
                if (carry == 1):
                    result = "1" + result
                    carry = 0
                else:
                    result = "0" + result
            elif((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")):
                if(carry == 1):
                    result = "0" + result
                else:
                    result = "1" + result
            else:
                if(carry == 1):
                    result = "1" + result
                else:
                    result = "0" + result
                    carry = 1
        if(carry == 1):
            result = "1" + result
            carry = 0
        return result