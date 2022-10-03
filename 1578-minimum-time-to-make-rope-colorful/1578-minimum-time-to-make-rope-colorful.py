class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        colors = "aabaa", neededTime = [1,2,3,4,1]
                   ||
                  ans = 1 + 1
                  collected = 5 - 4
                  max = max(4, 1, max)
        
        """
        
        ans = 0
        collected = maxim = 0
        
        for i in range(len(colors) - 1):
            # consecative colors same
            maxim = max([maxim, neededTime[i]])
            collected += neededTime[i]

            if colors[i] != colors[i + 1]:
                ans += (collected - maxim)
                collected = maxim = 0
    
        if len(neededTime) > 1 and colors[-1] == colors[-2]:
            collected += neededTime[-1]
            maxim = max(maxim, neededTime[-1])
        # print(ans, collected, maxim)
        return ans + (collected - maxim)