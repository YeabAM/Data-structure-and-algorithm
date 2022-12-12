# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = [0]
        
        def dfs(node, match):
            
            if not node:
                return
            
            match = match ^ (1 << node.val)
            
            if not node.right and not node.left:
                if match & (match - 1) == 0:
                    count[0] += 1
                        
                        
            
            left = dfs(node.left, match)
            right = dfs(node.right, match)
            

        
        dfs(root, 0)
        
        return count[0]
        
            
            