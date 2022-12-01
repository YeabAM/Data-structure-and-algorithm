class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #for recA
        leftBottomA = (ax1,ay1)
        rightTopA = (ax2, ay2)
        rightBottomA = (ax2, ay1)
        leftTopA = (ax1,ay2)
        
        #for recB
        leftBottomB = (bx1,by1)
        rightTopB = (bx2, by2)
        rightBottomB = (bx2, by1)
        leftTopB = (bx1,by2)
        
        #intersection width
        leftInt = max(leftBottomA[0], leftBottomB[0])
        rightInt = min(rightBottomA[0], rightBottomB[0])
        widthInt = rightInt - leftInt
        
        #intersection height
        topInt = min(rightTopA[1], rightTopB[1])
        bottomInt = max(rightBottomA[1], rightBottomB[1])
        heightInt = topInt - bottomInt
        
        areaInt = widthInt * heightInt if widthInt > 0 and heightInt > 0 else 0
        
        totalArea = (abs(ay1 - ay2) * abs(ax1 - ax2)) + (abs(by1 - by2) * abs(bx1 - bx2))
        
        CoverArea = totalArea - areaInt
        
        return CoverArea
        
        
        
        
        
        
        