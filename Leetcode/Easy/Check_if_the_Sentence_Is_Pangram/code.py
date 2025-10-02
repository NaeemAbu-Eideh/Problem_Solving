class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        alf = "abcdefghijklmnopqrstuvwxyz"
        for i in alf:
            if not i in sentence:
                return False
        return True
