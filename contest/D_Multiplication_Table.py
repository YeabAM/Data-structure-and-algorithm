rows, cols, k = map(int, input().split())

currCol = (k % cols) 
currRow = (k // cols) + 1
print(currRow, currRow)
if currCol == 1:
    possCol = 3
else:
    possCol = currCol - 1

possRow = currRow - 1

if possRow * possCol > currCol * currRow:
    print(possRow * possCol)
else:
    print(currCol * currRow)