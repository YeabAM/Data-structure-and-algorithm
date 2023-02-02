class Solution:
    def numberOfWays(self, string: str) -> int:
        forward = [[0, 0] for _ in range(len(string) + 1)]
        backward = [[0, 0] for _ in range(len(string) + 1)]

        for i in range(1, len(string) + 1):
            if string[i - 1] == '0':
                forward[i][0] = forward[i-1][0] + 1
                forward[i][1] = forward[i-1][1]
            else:
                forward[i][1] = forward[i-1][1] + 1
                forward[i][0] = forward[i-1][0]

        for j in range(len(string) - 1, -1, -1):
            if string[j] == '0':
                backward[j][0] = backward[j+1][0] + 1
                backward[j][1] = backward[j+1][1]
            else:
                backward[j][1] = backward[j+1][1] + 1
                backward[j][0] = backward[j+1][0]
        
        count = 0
        for k in range(len(string)):
            if string[k] == '0':
                count += forward[k+1][1] * backward[k][1]
                
            else:
                count += forward[k+1][0] * backward[k][0]
                
        return count
            
                