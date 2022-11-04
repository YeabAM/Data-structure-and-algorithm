from collections import deque
def solve():
    row, col = map(int, input().split())
    # print(row, col)
    graph = []
    visited = set()
    for _ in range(row):
        graph.append(list(input()))
    
    DIR = [(0,1),(0,-1),(1,0),(-1,0)]
    inbound = lambda r, c: 0 <= r < row and 0 <= c < col

 

    for r in range(row):
        for c in range(col):
            if (r, c) in visited:
                continue

            queue = deque()
            queue.append((r, c, None, None))

            while queue:
                cx, cy, px, py = queue.popleft()

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if (nx, ny) == (px, py) or not inbound(nx, ny) or graph[nx][ny] != graph[r][c]:
                        continue

                    if (nx, ny) in visited :
                        print("Yes")
                        return
                    else:
                        queue.append((nx, ny, cx, cy))
                        visited.add((nx, ny))

    print("No")

solve()
