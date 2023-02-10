class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counts = Counter(nums)
        pairings = 0
        visited = set()
        for i in range(1, len(target)):
            first = target[:i]
            second = target[i:]
            
            if (first, second) not in visited and (second, first) not in visited:
                visited.add((first, second))
                visited.add((second, first))
            
                if first in counts and second in counts:
                    # print(first, second)
                    # print(counts[first],counts[second],'count')

                    if first != second:
                        curr = (counts[first] * counts[second])
                        if second + first == target:
                             curr *= 2
                        
                        # print(curr,'crr')
                    else: 
                        curr = counts[first] *( counts[first] - 1)
                        # print(curr,'ecurr')

                    pairings += curr
                    

                
        return pairings
        