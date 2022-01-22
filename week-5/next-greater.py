class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}

        stack = [nums2[0]]
        

        for i in range(1, len(nums2)):
            # when stack not empty and current number greater than top of stack
            while stack and (nums2[i] > stack[-1]):
                greater_dict[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            greater_dict[stack.pop()] = -1

        return [greater_dict[i] for i in nums1]