class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        counts = Counter(arr)
        ans = [i for i in counts.values()]
        ans.sort(reverse = True)
        i = 0
        
        while i < len(ans) and size > len(arr) // 2:
            size -= ans[i]
            i += 1
            
        return i
        