class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []
        
        for i in s:
            if i == "#" and sStack:
                sStack.pop()
                print(sStack)
            elif i !="#":
                sStack.append(i)
                print(sStack)
        print("----------------")        
        for i in t:
            if i == "#" and tStack:
                tStack.pop()
                print(tStack)
            elif i !="#":
                tStack.append(i)
                print(tStack)
                
        return(tStack == sStack)
        
        