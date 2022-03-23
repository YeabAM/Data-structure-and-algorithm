class Solution(object):
    def partitionLabels(self, s: str) -> List[int]:
        lastIndices = dict()
        start = end = 0
        sizes = []
        for i, l in enumerate(s):
            lastIndices[l] = i
        
        for i, l in enumerate(s):
            end = max(end, lastIndices[l])
            if i == end:
                sizes.append(i - start + 1)
                start = i + 1
        
        return sizes