# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node.left and not node.right:
                return (node.val, node.val, 0)
            
            result = 0
            _min = node.val
            _max = node.val
            
            if node.left:
                left = dfs(node.left)
                _min = min(left[0], _min)
                _max = max(left[1], _max)
                result = max(abs(node.val - left[1]), abs(node.val - left[0]), left[2], result)
            
            if node.right:
                right = dfs(node.right)
                _min = min(right[0], _min)
                _max = max(right[1], _max)
                result = max(abs(node.val - right[1]), abs(node.val - right[0]), right[2], result)
            
            return (_min, _max, result)
        
        answer = dfs(root)
        
        return answer[2]