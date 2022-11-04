from email import message


msgSize, keySize, modSize = map(int, input().split())

msg = list(map(int, input().split()))
key = list(map(int, input().split()))

prefix = [0 for _ in range(msgSize)]

for i in range(keySize):
    prefix[i] += key[i]

    if (i + 1 < keySize):
        prefix[msgSize - keySize + i + 1] -= key[i]


msg[0] = (msg[0] + prefix[0]) % modSize

for i in range(1, msgSize):
    prefix[i] += prefix[i-1] 
    msg[i] = (msg[i] + prefix[i]) % modSize

print(*msg, sep=" ")