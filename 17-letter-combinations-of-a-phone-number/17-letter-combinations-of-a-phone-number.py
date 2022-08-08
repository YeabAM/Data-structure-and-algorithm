class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        comb = {
            2 : ["a","b","c"],
            3 : ["d","e","f"],
            4 : ["g","h","i"],
            5 : ["j","k","l"],
            6 : ["m","n","o"],
            7 : ["p","q","r","s"],
            8 : ["t","u","v"],
            9 : ["w","x","y","z"]
        }
        
        def backtrack (i, path):
            if len(digits) == 0:
                return
            
            if i == len(digits):
                result.append("".join(path))
                return
            
            
            for l in comb[int(digits[i])]:
                backtrack (i+1, path + [l])
                
                
            
        backtrack(0,[])
        
        return result
        