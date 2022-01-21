class Solution:
    def minOperations(self, logs: List[str]) -> int:
        directory = []
        
        for i in logs:
            if i == "../":
                if directory:
                    directory.pop()
            elif i != "./":
                directory.append(i)
        return len(directory)
            
            
        