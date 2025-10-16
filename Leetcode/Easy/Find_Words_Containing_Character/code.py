class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index = []
        length = len(words)
        for i in range(length):
            if x in words[i]:
                index.append(i)
        return index