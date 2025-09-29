class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        length = len(hours)
        count = 0
        for i in range(length):
            if(hours[i] >= target):
                count += 1
        return count