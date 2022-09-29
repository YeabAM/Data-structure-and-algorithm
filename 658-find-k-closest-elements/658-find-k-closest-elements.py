class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        difference = []
        
        for num in arr:
            heappush(difference, (abs(num - x), num))
            
        count = 0
        
        while count < k:
            candid = heappop(difference)
            ans.append(candid[1])
            count += 1
            
        return sorted(ans)