class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        
        for ops in logs:
            if ops == '../':
                if stack:
                    stack.pop()
                else:
                    continue
                    
            elif ops == './':
                continue
            else:
                stack.append(ops)
        
        print(stack)        
        return len(stack)