def col_num(col):
    place = 0
    total = 0
    for i in col[::-1]:
        total += (ord(i) - 64) * pow(26, place)
        place += 1
    print(total)