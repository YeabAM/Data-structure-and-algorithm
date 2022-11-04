case = int(input())

for _ in range(case):
    word = input()
    length = len(word)
    # print(word, "j")
    # print("f", word[:length // 2])
    # print("l",word[length // 2:])
    if length % 2 == 0:
        if word[:length // 2] == word[length // 2:]:
            
            print("YES")
        else:
            print("NO")

    else:
        print("NO")