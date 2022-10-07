class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        idx = 0
        
        # def checker(c1, c2):
        #     for letter in c1.items():
        #         if c2[letter] != c1[letter]:
        #             return False
        #     return True
        
        while idx < len(s1):
            counter1[s1[idx]] += 1
            counter2[s2[idx]] += 1
            idx += 1
        
        l = 0
        if counter1 == counter2:
            return True
        
        for i in range(idx, len(s2)):
            # print(counter2)
            counter2[s2[l]] -= 1
            counter2[s2[i]] += 1
            if counter2[s2[l]] == 0:
                del counter2[s2[l]]
            l += 1
            if counter1 == counter2:
                return True
            
        
        