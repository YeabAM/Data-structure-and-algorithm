class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1
        
        l, r = 0, 1
        
        flag = 1 if arr[0] > arr[1] else 0
        count = 1
        
        while r < len(arr):
            if arr[r-1] > arr[r] and flag == 1:
                count = max(count, r - l + 1)
                r += 1
                flag = 0
            
            elif arr[r-1] < arr[r] and flag == 0:
                count = max(count, r -l + 1)
                r += 1
                flag = 1
                
            else:
                if arr[r-1] == arr[r]:
                    l = r
                    r += 1
                else:
                    l = r-1
                    
                flag = 1 if r < len(arr) and arr[r-1] > arr[r] else 0
                
        return count
                    
                
                    
                    
        