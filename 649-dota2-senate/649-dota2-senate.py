class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Dsenate = deque()
        Rsenate = deque()
        totalSenate = len(senate)
        
        for i in range(totalSenate):
            if senate[i] == "R":
                Rsenate.append(i)
            else:
                Dsenate.append(i)
                
        while Rsenate and Dsenate:
            currD = Dsenate.popleft()
            currR = Rsenate.popleft()
            
            if currD < currR:
                Dsenate.append(totalSenate + currD)
            else:
                Rsenate.append(totalSenate + currR)
                
        if Dsenate:
            return "Dire"
        else:
            return "Radiant"