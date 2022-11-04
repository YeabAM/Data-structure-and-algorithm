strLen, ops = map(int, input().split())

word = list(input())

left = 0
counts = [0,0]
maxSize = 0
for right in range(strLen):
    counts[ord(word[right]) - 97] += 1
    cur_len = right - left + 1

    while left < right and cur_len  - max(counts) > ops:
        leftChar = word[left]
        counts[ord(word[left] )- 97] -= 1
        left += 1
        cur_len = right - left + 1

    maxSize = max(maxSize, cur_len)

print(maxSize)



