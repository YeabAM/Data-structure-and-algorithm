class Solution(object):
    def movesToStamp(self, stamp, target):
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in range(N - M + 1):
            

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        while queue:
            i = queue.popleft()

            
            for j in range(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]: 
                    A[j][1].discard(i)
                    if not A[j][1]: 
                        ans.append(j)
                        for m in A[j][0]: 
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []