class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
    
        for file in path:
            if file != "" and file != "." and file != "..":
        
                stack.append(file)
            
            elif file == "..":
                if stack:
                    stack.pop()
                    
        return "/" + "/".join(stack)
            
        
        
        
