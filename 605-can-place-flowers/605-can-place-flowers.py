class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        
        if length == 1:
            if flowerbed[0]==0:
                count += 1
                n  -= 1
            

            
        else:
            if flowerbed[1] == flowerbed[0] == 0:
                flowerbed[0] = 1
                count += 1
            if flowerbed[length - 2] == flowerbed[length - 1] == 0:
                flowerbed[length - 1] = 1
                count += 1
                
            for i in range(1, length - 1):
                if flowerbed[i] == flowerbed[i + 1] == flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n
                