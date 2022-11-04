def main():
    t = int(input())
    for _ in range(t):
        st = int(input())
        maxx = float("inf")


        def bk(i, path, pathSum):
            maxx = float("inf")
            if pathSum > st:
                return float("inf")

            # print(i, pathSum)
            if pathSum == st: 
                return int("".join(path))

            for j in range(i + 1, 10):
                maxx = min(maxx, bk(j, path + [str(j)], pathSum + j))
                # print(maxx)
            return maxx
        
        maxx = bk(0, [], 0)
        print(maxx)

        
main()