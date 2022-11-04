from collections import deque
def main():
    cases = int(input())
    
    for _ in range(cases):
        count = 0
        empty = input()
        nodes, ops = map(int, input().split())
        if nodes == 1:
            print(0)
            continue
        graph = [set() for _ in range(nodes)]
        
        for _ in range(nodes - 1):
            n1, n2 = map(int, input().split())
            graph[n1 - 1].add(n2 - 1)
            graph[n2 - 1].add(n1 - 1)
        queue = deque()
    
        for i in range(nodes):
            if len(graph[i]) == 1:
                queue.append(i)
        leaf = []       
        while ops > 0 and queue:
                # print("ops", ops)
                length = len(queue)
                for _ in range(length):
                    curr = queue.popleft()
                    leaf.append(curr)
                    for negh in graph[curr]:
                        graph[negh].remove(curr)
                        # print(len(graph[negh]),"l")
                        if len(graph[negh]) == 1:
                            queue.append(negh)
                            
                ops -= 1
                 
        print(nodes - len(leaf))
        # print(leaf)
        # print(graph)
                 
                        
                
            
        
main()




    


