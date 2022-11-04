from collections import defaultdict, deque

def generate_keyboard(password):
    graph = defaultdict(set)
    isUsed = [0 for _ in range(26)]
    for i in range(1, len(password)):
            if password[i-1] in graph and password[i] in graph:
                if password[i-1] not in graph[password[i]]:
                    print("NO")
                    return
                
            elif len(graph[password[i-1]]) >= 2 or len(graph[password[i]]) >= 2:
                print("NO")
                return
            
            graph[password[i]].add(password[i-1])
            graph[password[i-1]].add(password[i])

    # print(graph)
    queue = deque()
    keyboard = []
    for char in graph:
        if len(graph[char]) == 1:
            queue.append(char)
            break

    while queue:
        currChar = queue.popleft()
        keyboard.append(currChar)
        isUsed[ord(currChar) - 97] = 1
        for adj in graph[currChar]:
            graph[adj].remove(currChar)
            queue.append(adj)

    for i in range(26):
        if isUsed[i] == 0:
            charr = chr(97 + i)
            keyboard.append(charr)
    print("YES")
    print("".join(keyboard))
    return


def main():
    test = int(input())

    for _ in range(test):
        
        password = list(input())
        generate_keyboard(password)

        
main()
