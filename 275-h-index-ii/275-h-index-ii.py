class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        hIndex = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            print(mid)
            
            if 0 <= len(citations) - mid - 1 <= len(citations) - 1:
                if citations[len(citations) - (mid + 1)] >= mid + 1:
                    hIndex = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
                
        return hIndex
                
            