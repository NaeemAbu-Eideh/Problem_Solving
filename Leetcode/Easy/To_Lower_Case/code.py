class Solution:
    def toLowerCase(self, s: str) -> str:
        string = ""
        for char in s:
            if(char >= 'A' and char <= 'Z'):
                num = ord(char)
                num += 32
                string += chr(num)
            else:
                string += char
        return string
            
