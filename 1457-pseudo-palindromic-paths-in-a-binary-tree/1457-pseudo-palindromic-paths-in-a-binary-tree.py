# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = [0]
        
        def dfs(node, match, size):
        
            if not node.right and not node.left:
                oddCount = 0
                match[node.val - 1] += 1
                size += 1
                
                
                for i in range(9):
                    if match[i] % 2:
                        oddCount += 1
                        
                if size % 2 and oddCount == 1:
                
                    count[0] += 1

                else:
                    if oddCount == 0:
                    
                        count[0] += 1
                        
            
                return 
            
                            
            match[node.val - 1] += 1
            left = right = 0
            
            if node.left:
                left = dfs(node.left, match.copy(), size + 1)
            if node.right:
                right = dfs(node.right, match.copy(), size + 1)
            

            return
        
        dfs(root, [0,0,0,0,0,0,0,0,0], 0)
        
        return count[0]
        
            
            