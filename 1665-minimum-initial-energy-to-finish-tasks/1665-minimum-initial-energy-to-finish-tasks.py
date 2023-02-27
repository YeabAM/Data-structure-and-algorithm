class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x : x[1] - x[0], reverse = True)
        
        def check(energy):

            for a, m in tasks:
                if energy < m:
                    return False
                else:
                    energy -= a
                
            return energy >= 0
        
        l = max([minm for a, minm in tasks])
        r = sum([minm for a, minm in tasks])
    
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
    
    
        