from collections import deque

def find(cell, parents):
    if parents[cell] == cell:
        return cell

    parents[cell] = find(parents[cell], parents)
    return parents[cell]

def union(ru, cu, rv, cv, parents, size):
    cellU = (ru, cu)
    cellV = (rv, cv)
    pu = find(cellU, parents)
    pv = find(cellV, parents)

    # print("prnts", pu, pv, cellU, cellV)

    if pu != pv:
        if size[pu] >= size[pv]:
            size[pu] += size[pv]
            parents[pv] = pu

        else:
            size[pv] += size[pu]
            parents[pu]= pv





def main():
    rows, cols = map(int, input().split())
    matrix = []
    size = {}
    parents = {}
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
    for _ in range(rows):
        matrix.append(list(input()))

    for r in range(rows):
        for c in range(cols):
            cell = (r, c)
            parents[cell] = cell
            size[cell] = 1

    # print(size)

    #union all the empty spaces
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '.':
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if in_bound(nr, nc) and matrix[nr][nc] == '.':
                        union(r, c, nr, nc,parents, size)

    #iterate over obstace and check adjacent empty cells and add their size
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '*':
                prnt = set()
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if in_bound(nr, nc) and matrix[nr][nc] == '.':
                        cell = (nr,nc)
                        prnt.add(find(cell, parents))

                count = 0
                for pr, pc in prnt:
                    count += size[(pr, pc)]

                matrix[r][c] = str((count + 1) % 10)
                    

    for r in range(rows):
        print("".join(matrix[r]))


    

main()







    