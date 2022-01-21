class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scoreStack = []
        for i in range(len(ops)):
            if ops[i] == "C":
                scoreStack.pop()
            elif ops[i] == "D":
                temp = scoreStack.pop()
                scoreStack.append(temp)
                scoreStack.append(2*temp)
            elif ops[i] == "+":
                temp1 = scoreStack.pop()
                temp2 = scoreStack.pop()
                scoreStack.append(temp2)
                scoreStack.append(temp1)
                scoreStack.append(temp1 + temp2)
            else:
                scoreStack.append(int(ops[i]))
                
        finalStack = sum(scoreStack)
        
        return finalStack