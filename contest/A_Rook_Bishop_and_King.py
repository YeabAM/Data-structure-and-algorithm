from collections import deque


r1, c1, r2, c2 = map(int, input().split())


#for rook
def rook(r1, c1, r2, c2):
    rook = 0
    if r1 == r2 or c1 == c2:
        rook = 1
        return rook
    else:
        rook = 2
        return rook

#for bishop
def bis(r1, c1, r2, c2):
    bishop = 0
    isDiagonal = abs(r2 - r1) // abs(c2 - c1)
    if isDiagonal == 1:
        bishop = 1
        return bishop

    beg = 0
    end  = 0
    if r1 % 2 == c1 % 2:
        beg = 0

    if r2 % 2 == c2 % 2:
        end = 0
    
    elif r1 % 2 != c1 % 2:
        beg = 1

    elif r2 % 2 != c2 % 2:
        end = 1

    if beg != end:
        bishop= 0
        return bishop
    else:
        bishop = 2
        return bishop


    


#for king
def king(r1, c1, r2, c2):
  
    king = 0
    direction = [(0, 1),(1, 0),(0,-1),(-1,0), (1, -1),(-1, 1),(1, 1),(-1, -1)]
    inbound = lambda r, c: 1 <= r <= 8 and 1 <= c <= 8
    queue = deque()
    queue.append((r1, c1))
    visited = set()
    visited.add((r1, c1))

    while queue:
        # print(king, "king")
        for _ in range(len(queue)):
            cx, cy = queue.popleft()
            # print(cx, cy,"end")
            if cx == r2 and cy == c2:
                return king

            for dx, dy in direction:
                nx, ny = dx + cx, dy + cy
                # print(nx, ny)
                if inbound (nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    

        king += 1
    
    return king

print(rook(r1, c1, r2, c2), bis(r1, c1, r2, c2),king(r1, c1, r2, c2 ))

