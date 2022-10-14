# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        isEven = True
        
        while queue:
            running = []
            length = len(queue)
            
            for _ in range(length):
                curr = queue.popleft()
                
                running.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
        
                if curr.right:
                    queue.append(curr.right)
    
            if isEven:
                isEven = not isEven
                for i in range(len(running)):
                    if not running[i] % 2 or ( i > 0 and running[i] <= running[i-1]):
                        return False
                continue
            
            else:
                isEven = not isEven
                for i in range(len(running)):
                    if running[i] % 2 or ( i > 0 and running[i] >= running[i-1]):
                        return False
                continue
                
        return True
            
            
                
                
                
        