# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer = []
        result = []
        index = 0
        while head:
            
            while stack and stack[-1][1] < head.val:
                temp = stack.pop()
                answer[temp[0]] = head.val
                
            stack.append([index, head.val])
            answer.append(0)
            index += 1
            head = head.next
            
        return answer