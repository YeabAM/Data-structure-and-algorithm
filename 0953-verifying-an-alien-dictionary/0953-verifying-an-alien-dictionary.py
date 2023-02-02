class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        
        for i in range(len(order)):
            ordering[order[i]] = i
            
        right_ordering = []
        
        for word in words:
            temp = []
            for w in word:
                temp.append(ordering[w])
            right_ordering.append(temp)
            
        return right_ordering == sorted(right_ordering)
                