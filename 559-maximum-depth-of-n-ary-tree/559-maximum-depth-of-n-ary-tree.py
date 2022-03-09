# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
# """
#  /   _____/ ___________  ____ |  | |  |                             
#  \_____  \_/ ___\_  __ \/  _ \|  | |  |                             
#  /        \  \___|  | \(  <_> |  |_|  |__                           
# /_______  /\___  |__|   \____/|____|____/                           
#   _____ \/     \/                .__          __  .__               
# _/ _______________    __________ |  |  __ ___/  |_|__| ____   ____  
# \   __/  _ \_  __ \  /  ___/  _ \|  | |  |  \   __|  |/  _ \ /    \ 
#  |  |(  <_> |  | \/  \___ (  <_> |  |_|  |  /|  | |  (  <_> |   |  \
#  |__| \____/|__|    /____  \____/|____|____/ |__| |__|\____/|___|  /
#                          \/                                      \/ 
# class Solution:
#     def __init__(self):
#         self.maxDepth = 0
#     def maxDepth(self, root: 'Node') -> int:
#         def dfs(root):
#             if not root:
#                 return 0
#             if not root.children:
#                 return 1
#             for child in root.children:
#                 dp = 1 + dfs(child)
#                 if maxDepth < dp:
#                     maxDepth = dp 
#                 self.maxDepth = max(1 + dfs(child),)
#         dfs(root)
#         return maxDepth


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root:
                return 0
            dp = 1
            for child in root.children:
                dp = max(dp,1 + dfs(child))
            return dp                        
        return dfs(root)




