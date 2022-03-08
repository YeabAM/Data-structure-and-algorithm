# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total =[]
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.total.append(abs(left - right))
            
            return root.val + left + right
        dfs(root)
        return sum(self.total)

        
        
            
            
        