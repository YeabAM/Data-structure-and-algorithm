class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original = []
        count = Counter(changed)
        print(count)
        if len(changed) %2 == 0:
            for i in changed:
                if count[i] > 0 and count[2*i] > 0:              
                    if i != 0:
                        original.append(i)
                        count[i] -= 1
                        count[2*i] -= 1                    
                    elif count[i] > 1:
                        original.append(i)
                        count[i] -= 1
                        count[2*i] -= 1
                        
                                        
        if len(changed) // 2 == len(original):
            return original
        else:
            return []