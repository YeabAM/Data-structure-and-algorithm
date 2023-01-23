class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        truster = defaultdict(int)
        trustee = defaultdict(int)
        
        for trust, who in trust:
            truster[trust] += 1
            trustee[who] += 1
            
        for person in range(1, n+1):
            if truster[person] == 0 and trustee[person] == n - 1:
                return person
            
        return -1
        