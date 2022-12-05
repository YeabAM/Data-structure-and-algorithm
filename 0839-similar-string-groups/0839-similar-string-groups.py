class Solution:
    def isSimilar(self,word1, word2):
        count = 0
        
        for idx in range(len(word1)):
            if word1[idx] != word2[idx]:
                count += 1
                
        return count <= 2
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        #define parents for each words, setting each parent of their own
        parents = {}
        rank = {}
        
        for word in strs:
            parents[word] = word
            rank[word] = 1
        
        
        def find(word):
            if parents[word] == word:
                return word
        
            parents[word] = find(parents[word])

            return parents[word]
        
        def union(w1, w2):
            p1 = find(w1)
            p2 = find(w2)
            
            if p1 != p2:
                if rank[p1] <= rank[p2]:
                    parents[p1] = p2
                    rank[p1] += rank[p2]
                else:
                    parents[p2] = p1
                    rank[p2] += p1
            
            
        for i in range(len(strs)):
            for j in range(len(strs)):
                if self.isSimilar(strs[i], strs[j]):
                    union(strs[i], strs[j])
                    
        
        groups = set()
        
        for words in strs:
            groups.add(find(words))
            
        numOfGroups = len(groups)
        
        return numOfGroups