class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited1 = set()
        visited2 = set()
        ans = set()
        
        while node1 != -1 or node2 != -1:
            if node1 != -1 and ((node1 in visited2) or node1 == node2):
                ans.add(node1)
            if node2 != -1 and ((node2 in visited1) or node1 == node2):
                ans.add(node2)
            if ans:
                return min(ans)
            if node1 != -1 and node1 not in visited1:
                visited1.add(node1)
                node1 = edges[node1]
            else:
                node1 = -1
            if node2 != -1 and node2 not in visited2:
                visited2.add(node2)
                node2 = edges[node2]
            else:
                node2 = -1
        return -1