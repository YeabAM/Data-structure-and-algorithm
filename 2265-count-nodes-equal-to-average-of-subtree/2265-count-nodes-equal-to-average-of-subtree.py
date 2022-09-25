# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node.right and not node.left:
                ans += 1
                return (node.val, 1)
            
            else:
                if node.left:
                    left = dfs(node.left)
                else:
                    left = (0,0)
                if node.right:
                    right = dfs(node.right)
                else:
                    right = (0,0)
                
                summ = left[0] + right[0] + node.val
                numOfNodes = right[1] + left[1] + 1
                
                if node.val == summ // numOfNodes:
                    ans += 1
                    
                return (summ, numOfNodes)
        
        dfs(root)
        
        return ans
        