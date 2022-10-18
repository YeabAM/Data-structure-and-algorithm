class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #total garbage collected
        totalGarbage = 0
        
        # amount of travel cost of each garbage truck
        paperGarbage = 0
        glassGarbage = 0
        metalGarbage = 0
        
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
            
        for i , assortment in enumerate(garbage):
            currTotalGarbage = len(assortment)
            totalGarbage += currTotalGarbage
            
            currPaperGarbage = assortment.count('P')
            currGlassGarbage = assortment.count('G')
            currMetalGarbage = assortment.count('M')
            
            if i > 0:
                if currPaperGarbage > 0:
                    paperGarbage = travel[i - 1]

                if currGlassGarbage > 0 :
                    glassGarbage = travel[i - 1]

                if currMetalGarbage > 0 :
                    metalGarbage = travel[i - 1]
                    
        totalTime = paperGarbage + glassGarbage + metalGarbage + totalGarbage
        
        return totalTime

            