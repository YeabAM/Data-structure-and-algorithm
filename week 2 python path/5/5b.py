def col_alp(col):
    s = []
    while col:
        col -= 1
        s.append(chr((col % 26) + 65))
        col //= 26
    print("".join(s[::-1]))