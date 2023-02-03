# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        ans = []
        queue = deque()
        queue.append((root, 0, 0,0))
        
        
        while queue:
            node, r, c, level = queue.popleft()
            
            cols[c].append([level,node.val])
            
            if node.left:
                left = (node.left, r+1, c-1, level + 1)
                queue.append(left)
            
            if node.right:
                right = (node.right, r+1, c+1, level + 1)
                queue.append(right)
                
        for key in sorted(cols.keys()):
            ans.append(list(map(lambda x: x[1], sorted(cols[key]))))
            
        return ans
            
        