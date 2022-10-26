class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        stack.append(-1)
        maxLength = 0
        for idx, char in enumerate(s):
            # print(stack)
            if char == "(":
                stack.append(idx)
            else:
                stack.pop()
                # print(stack,"y")
                if not stack:
                    stack.append(idx)
                else:
                    # print(stack[0])
                    maxLength = max(maxLength, idx - stack[-1])
                    
                    
            # print(stack)
                    
        return maxLength
                
             