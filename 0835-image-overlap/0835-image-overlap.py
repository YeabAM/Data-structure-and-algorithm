class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        points_a=[] 
        points_b = []
        dist = collections.defaultdict(int)
        
        rows = len(img1)
        cols = len(img1[0])
               
        for r in range(rows):
            for c in range(cols):
                if img1[r][c]:
                    points_a.append((r, c))

                if img2[r][c]:
                    points_b.append((r, c))

        for r, c in points_a:
            for r2, c2 in points_b:
                dist[(r2 - r, c2 - c)] += 1

        
        
        if dist.values():
            return max(dist.values())
        
        return 0
    

    
        
        
        
        
        
        
        
        