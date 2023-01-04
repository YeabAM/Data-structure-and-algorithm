class Solution:
    #anything beyond 1 the remaing of number divided by 3 is divisble by 2, like 11, 11 - 9 = 2, 23, 23-21 = 2
    def minimumRounds(self, tasks: List[int]) -> int:
        freqs = Counter(tasks)
        rounds = 0
        
        for dif in freqs:
            if freqs[dif] == 1:
                return -1
            
            amount = freqs[dif] // 3
            
            if freqs[dif] % 3 == 0 and freqs[dif] >= 3:
                # print(dif, 'odd')
                rounds += amount
            else:
                # print(dif,'even')
                rounds += amount + 1
                
            # print(rounds,'r')
                
        return rounds
        