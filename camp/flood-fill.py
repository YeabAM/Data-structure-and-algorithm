class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row, col):
            image[row][col] = newColor
            visited.add((row, col))
            for direction in DIR:
                newRow, newCol = row + direction[0], col + direction[1]
                if (newRow, newCol) in visited or not in_bound(newRow, newCol) or image[newRow][newCol] != startColor:
                    continue
                dfs(newRow, newCol)
                
        in_bound = lambda row, col : 0 <= row < len(image) and 0 <= col < len(image[0])
        visited = set((sr, sc))
        startColor = image[sr] [sc]
        DIR = [[1,0], [0,1],[-1,0],[0,-1]]
        image[sr][sc] = newColor
        dfs(sr, sc)
        print(visited)
        return image
        