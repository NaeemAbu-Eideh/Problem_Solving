class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i = 0
            j = len(word)-1
            while(i != j and i != j+1):
                if(word[i] != word[j]):
                    break
                i += 1
                j-=1
            if(i == j+1 or i == j):
                if(word[i] != word[j]):
                    return False
                return word
        return ""
            