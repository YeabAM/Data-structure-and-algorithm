cases = int(input())
   
for _ in range(cases):
    n = int(input())
    parents = list(map(int, input().split()))

    if len(parents) == 1:
        print('1\n1\n1'); continue

    leaves = set(i + 1 for i in range(n)) - set(parents)
    print(len(leaves))

    visited = set()
    for leaf in leaves:
        cur = leaf
        path = [leaf]
        while parents[cur - 1] != cur:
            cur = parents[cur - 1]
            if cur in visited:
                break
            visited.add(cur)
            path.append(cur)

        print(len(path))
        print(' '.join(map(str, reversed(path))))