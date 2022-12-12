# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = [0,0]
        
        def dfs(node, level):
            if not node:
                return
            
            if level > ans[0]:
                ans[1] = node.val
                ans[0] = level
                
            elif level == ans[0]:
                ans[1] += node.val
                
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
            
        dfs(root, 1)
        
        return ans[1]
        
    
            
            