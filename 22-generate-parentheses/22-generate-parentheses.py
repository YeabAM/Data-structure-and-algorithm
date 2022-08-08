class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        op, cl = 0, 0
        
        def backt(path, op, cl):
                
            if len(path) // 2 == n:
                result.append("".join(path))
                
            if op < n:
                backt(path + ["("], op + 1, cl)
                
            if cl < op:
                backt(path + [")"], op, cl + 1)
        
        
        backt([], 0 , 0)    
        return result
        
        
        