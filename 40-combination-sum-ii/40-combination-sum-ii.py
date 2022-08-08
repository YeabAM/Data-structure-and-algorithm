class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = Counter(candidates)
        keys = list(count.keys())
        
        def backtrack(idx, total, path):
            if total > target:
                return
            if total == target:
                result.append(path)
                return
            
            for i in range(idx, len(keys)):
                if count[keys[i]] == 0:
                    continue
                count[keys[i]] -= 1
                backtrack(i, total + keys[i], path + [keys[i]])
                count[keys[i]] += 1
                
        result = []
        backtrack(0, 0, [])
        return result