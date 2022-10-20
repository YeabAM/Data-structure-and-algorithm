class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefixSum = [0]
        size = len(arr)
        count = 0
        
        for i in range(size):
            prefixSum.append(prefixSum[-1] + arr[i])
        
        
        for i in range(0, len(prefixSum) - k):
            currSum = prefixSum[i + k] - prefixSum[i]
            if currSum // k >= threshold:
                count += 1
                
        return count
        
            