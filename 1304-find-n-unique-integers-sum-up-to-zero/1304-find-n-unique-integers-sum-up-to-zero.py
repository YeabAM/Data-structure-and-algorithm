class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        count = 0
        while count < (n // 2):
            arr.append((count + 1)*-1)
            count += 1
        
        if n % 2:
            arr.append(0)
            
        for n in arr[:(n // 2)]:
            arr.append(-1 * n)
            
        return arr
        
        