l, r = map(int, input().split())


bitLength = (l ^ r).bit_length()
# print(bitLength, l ^ r)
large = 2 ** bitLength

if l != r:
    print(large - 1)
else:
    print(0)

