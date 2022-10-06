class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        size = len(tiles)
        #sort the tiles
        tiles.sort()
        #prefix sum of number of tiles per each
        prefixSum = [0]
        ans = float('-inf')
        for beg, end in tiles:
            prefixSum.append(prefixSum[-1] + end - beg + 1)
            
        #itertae thru each tiles
        for i, (beg, end) in enumerate(tiles):
            target = beg + carpetLen
            idx = self.search(target, tiles)
            if tiles[idx][1] < target:
                ans = max(ans,prefixSum[idx + 1] - prefixSum[i])
            else:
                ans = max(ans, prefixSum[idx] - prefixSum[i] + target - tiles[idx][0])
            
            
        return ans
        
    #define binary search
    def search(self, target, tiles):
        left = 0
        right = len(tiles) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if tiles[mid][0] < target <= tiles[mid][1]:
                return mid
            
            if tiles[mid][0] == target:
                return mid -1 
            
            if tiles[mid][0] > target:
                right = mid - 1
                
            elif tiles[mid][1] < target:
                left = mid + 1
        # print(left, right)        
        return left - 1
                
        
            
        
        
        