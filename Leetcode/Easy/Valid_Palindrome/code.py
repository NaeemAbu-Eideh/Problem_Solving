class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for i in range(len(s)):
            if((s[i] >= "A" and s[i] <= "Z") or (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9")):
                s2 += s[i]
        s2 = s2.lower()
        i = 0
        if(len(s2) == 0):
            j = 0
        else:
            j = len(s2)-1
        while(i != j and i != j+1):
            if(s2[i] != s2[j]):
                return False
            i+=1
            j-=1
        if(i == j+1):
            if(s2[i] != s2[j]):
                return False
        return True