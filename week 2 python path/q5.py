def do_pattern(H):
    space = H
    for i in range(H):
        clm = (2 * i) + 1
        for j in range(1, clm+1):
            print(" " * space,end=" ")
            print(j,end="")
        space -= 1
        print(" ")

do_pattern(4)