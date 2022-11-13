class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        # cannot have K sets with equal sum
        if total % k:
            return False
        
        target = total // k
        visited = 0
        visited |= (1 << 0)
        nums.sort(reverse = True)
        
        def backtrack(index, count, subsetSum, visited):
            if count == 0:
                return True
            #found one subset with sum equals to target
            if subsetSum == target:
                return backtrack(0, count - 1, 0, visited)
            
            found = False
            i = index + 1
            currSum = 0
            while not found and i < len(nums):
                currSum = nums[i] + subsetSum
                if not visited & (1 << i) and currSum <= target:
                    visited |= (1 << i)
                    found |= backtrack(i, count, currSum, visited)
                    visited &= ~(1 << i)
                    
                i += 1
                
            return found
        
        isPossible = backtrack(0, k, nums[0], visited)
        
        return isPossible
        
        
        