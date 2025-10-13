class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        length = len(arr)
        for i in range(length):
            if arr[i] % 2 == 1:
                if(i+1 < length and i+2 < length and arr[i+1]%2 == 1 and arr[i+2] %2 == 1):
                    return True
        return False