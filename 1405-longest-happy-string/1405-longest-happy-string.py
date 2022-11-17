class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        ans = []
        
        
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(heap, (count,char))
                
        
        while heap:
            curr, char = heapq.heappop(heap)
            
            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                if not heap:
                    break
                    
                nxtCurr, nxtChar = heapq.heappop(heap)
                
                ans.append(nxtChar)
                nxtCurr += 1
                
                if nxtCurr:
                    heapq.heappush(heap, (nxtCurr, nxtChar))
                    
            else:
                ans.append(char)
                curr += 1
                
            if curr:
                heapq.heappush(heap, (curr, char))
                
        
        
        return "".join(ans)
            