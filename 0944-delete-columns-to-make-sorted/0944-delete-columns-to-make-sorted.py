class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        a=0
        b=[]
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                b.append(strs[j][i])
            if(b!=sorted(b)):
                a=a+1
                b=[]
            else:
                b=[]
        return a