class Solution:
    def minimumDeleteSum(self, text1: str, text2: str) -> int:    
        memo = {}
        
        def topDown(index1, index2):
            if index1 > len(text1) - 1 and index2 > len(text2) - 1:
                return 0
            
            check = False
            if index1 <= len(text1) - 1 and index2 <= len(text2) -1:
                check = text1[index1] == text2[index2]
            
            if index1 == len(text1) - 1 and index2 == len(text2) - 1:
                if check:
                    return 0
                else:
                    return ord(text1[-1]) + ord(text2[-1])
            
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            
            result = inf
            if check:
                result = topDown(index1 + 1, index2 + 1)
                memo[(index1, index2)] = result
                return result
            
            else:
                if index1 < len(text1):
                    result = min(result, ord(text1[index1]) + topDown(index1 + 1, index2))
                
                if index2 < len(text2):
                    result = min(result, ord(text2[index2]) + topDown(index1, index2 + 1))
                    
            memo[(index1, index2)] = result
            return result
        
        answer = topDown(0,0)
            
        return answer