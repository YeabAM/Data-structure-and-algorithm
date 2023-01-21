class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(idx, vals):
            if len(vals) == 4 and idx == len(s):
                res.append(".".join(vals))
                return
            
            if len(vals) == 4 or idx == len(s):
                return
            
            if s[idx] == '0':
                vals.append('0')
                backtrack(idx + 1, vals)
                del vals[-1]
                return
            
            j = idx
            
            while j < len(s) and 0 < int(s[idx:j+1]) <= 255:
                vals.append(s[idx:j+1])
                backtrack(j + 1, vals)
                del vals[-1]
                j += 1
                
        backtrack(0, [])
        
        return res
            
            
        