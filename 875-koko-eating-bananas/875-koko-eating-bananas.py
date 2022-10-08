class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minn = ceil(sum(piles) / h)
        maxx = max(piles)
        
        while minn <= maxx:
            curr = minn + (maxx - minn) // 2
            total = 0
            ans = float('inf')
            
            # print(minn, maxx, "edge")
            for pile in piles:
                total += ceil(pile / curr)
            
            if total <= h:
                ans = min(ans, curr)
                maxx = curr - 1
                
            else:
                minn = curr + 1
            # else:
            #     ans = min(ans, curr)
            #     maxx = curr - 1
             
        return min(ans, minn)
                
            
            
        
        