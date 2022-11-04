import sys, threading
def main():
    
    from collections import defaultdict,deque

    n, m = map(int,input().split())
    cats = list(map(int, input().split()))
    graph = defaultdict(set)

    for _ in range(n-1):
        a, b = map(int,input().split())
        graph[a].add(b)
        graph[b].add(a)

    answer = 0

    def dfs(node, count):
        nonlocal answer
        if cats[node-1]:
            count += 1
        else:
            count = 0
        
        if count > m:
            return

        if not graph[node] and count <= m:
            answer += 1
            return

        for neighbour in graph[node]:
            graph[neighbour].remove(node)
            dfs(neighbour, count)

    dfs(1,0)
    print(answer)

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()