class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if self.isOperator(val):
                operand1 = stack.pop()
                operand2 = stack.pop()

                if val == '/':
                    res = int(operand2 / operand1)
                    stack.append(res)
                
                elif val == '+':
                    res = operand2 + operand1
                    stack.append(res)
                
                elif val == '-':
                    res = operand2 - operand1
                    stack.append(res)
                
                else:
                    res = operand2 * operand1
                    stack.append(res)
            
            else:
                stack.append(int(val))
        
        return stack.pop()
    
    def isOperator(self, val):
        return val == '+' or val == '-' or val == '*' or val == '/'