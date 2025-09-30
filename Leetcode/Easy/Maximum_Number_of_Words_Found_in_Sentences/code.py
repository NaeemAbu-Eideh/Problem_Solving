class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        length = len(sentences)
        for i in range(length):
            arr = sentences[i].split()
            if count < len(arr):
                count = len(arr)
        return count