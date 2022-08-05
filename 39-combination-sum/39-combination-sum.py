class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(idx, candis):
            summ = sum(candis)
            if  summ == target:   
                result.append(candis[::])
                # print(idx, candis,result)
            elif sum(candis) < target:
                for i in range(idx, len(candidates)):   
                    if summ + candidates[i] <= target:
                        candis.append(candidates[i])
                        backtrack(i, candis) 
                        candis.pop()
                        
                    else:
                        break
                        
        backtrack(0, [])
        return result
            
        