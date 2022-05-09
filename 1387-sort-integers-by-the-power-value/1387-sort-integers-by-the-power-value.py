from functools import lru_cache 
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        counts = []
        @lru_cache(None)
        
        def dp(num, count):
            # print(num, count)
            if num == 1:
                return count
            
            elif num % 2 == 0:
                count += 1
                return dp(num // 2, count)
                
            else:
                count += 1
                return dp(3 * num + 1, count)
            
        # x = dp(lo, 0)
        # print(x)
        for n in range(lo, hi+1):
            counts.append((n, dp(n, 0)))
            
        # print(counts)
        counts.sort(key = lambda x: x[1])
        return counts[k-1][0]
            
            
                
        