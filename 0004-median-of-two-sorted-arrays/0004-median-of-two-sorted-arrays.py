class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        
        a, b = nums1, nums2
        
        if len(a) > len(b):
            a, b = b, a
        
        l, r= 0, len(a) - 1
        
        while True:
            mid = l + ((r - l) // 2)
            midB = half - mid - 2
            
            aLeft = a[mid] if mid >= 0 else float('-inf')
            aRight = a[mid + 1] if (mid + 1) < len(a) else float('inf')
            bLeft = b[midB] if midB >= 0 else float('-inf')
            bRight = b[midB + 1] if (midB + 1) < len(b) else float('inf')
            
            #correct partition
            if aLeft <= bRight and bLeft <= aRight:
                #odd
                if total % 2:
                    return min(aRight, bRight)
                
                #even
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            
            elif aLeft > bRight:
                r = mid - 1
                
            else:
                l = mid + 1
                
        
                
            