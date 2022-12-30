# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        
        def dfs(node):
            nonlocal max_sum
            
            if not node.right and not node.left:
                # min max sum
                max_sum = max(max_sum, node.val)
                return (node.val, node.val, node.val)
            
            left = dfs(node.left) if node.left else (float('-inf'), float('-inf'), 0)
            right = dfs(node.right) if node.right else (float('inf'), float('inf'), 0)
            
            if left[1] < node.val < right[0]:
                summ = node.val + left[2] + right[2]
                max_sum = max(max_sum, summ)
                leftB = left[0] if left[0] != float("-inf") else node.val
                rightB = right[1] if right[1] != float("inf") else node.val
                return (leftB, rightB, summ)
            
            return (min(node.val, left[0]), max(node.val, right[1]), float("-inf"))
        
        dfs(root)
        '''
        
        '''
        
        return max_sum