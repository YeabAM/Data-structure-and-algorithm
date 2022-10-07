class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return []
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        idx = 0
        
        
        while idx < len(p):
            counter1[p[idx]] += 1
            counter2[s[idx]] += 1
            idx += 1
        
        
        if counter1 == counter2:
            ans.append(0)
            
        l = 0
        for i in range(idx, len(s)):
            # print(counter2)
            counter2[s[l]] -= 1
            counter2[s[i]] += 1
            if counter2[s[l]] == 0:
                del counter2[s[l]]
            l += 1
            if counter1 == counter2:
                ans.append(l)
                
        return ans
        