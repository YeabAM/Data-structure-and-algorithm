class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        direction = 1
        cur = 1
        pos = {}
        for i in range(n-1,-1,-1):
            if direction == 1:
                for j in range(n):
                    pos[cur] = (i,j)
                    cur += 1
            else:
                for j in range(n-1,-1,-1):
                    pos[cur] = (i,j)
                    cur += 1

            direction *= -1

        queue = [1]
        visited = set()
        res = 0
        found = False
        while len(queue) > 0:
            temp = []

            for num in queue:
                for i in range(1,7):
                    if num+i >= n*n:
                        found = True
                        break
                    
                    r,c = pos[num+i]
                    if board[r][c] != -1:
                        if board[r][c] not in visited:
                            temp.append(board[r][c])
                            visited.add(board[r][c])
                            if board[r][c] >= n*n:
                                found = True
                                break
                        continue
                    if num+i in visited:continue
                    temp.append(num+i)
                    visited.add(num+i)
            
            res += 1
            if found: break
            queue = temp
        if not found: return -1
        return res