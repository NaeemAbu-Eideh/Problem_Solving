class Solution:
    def judgeCircle(self, moves: str) -> bool:
        point = [0,0]
        for i in moves:
            if(i == 'L'):
                point[0] -= 1
            elif(i == 'R'):
                point[0] += 1
            elif(i == 'U'):
                point[1] += 1
            else:
                point[1] -= 1
        if(point == [0, 0]):
            return True
        return False