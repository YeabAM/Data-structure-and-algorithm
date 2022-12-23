# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        total_coins = 0
        
        def distribute(node):
            
            nonlocal total_coins
        
            if not node:
                return 0

            left = distribute(node.left)
            right = distribute(node.right)

            total_coins += abs(left) + abs(right)  

            return (left + right + node.val) - 1
        
        
        distribute(root)
        
        return total_coins
        