class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        dislike = defaultdict(list)
        
        parent = [i for i in range(n + 1)]
        rank = [1 for _ in range(n+1)]
        
        for p1, p2 in dislikes:
            dislike[p1].append(p2)
            dislike[p2].append(p1)
            
            
        def find(person):
    
            if parent[person] == person:
                return person
            
            parent[person] = find(parent[person])
            
            return parent[person]
        
        def union(person_1, person_2):
        
            p1 = find(person_1)
            p2 = find(person_2)
            
            if p1 != p2:
                
                if rank[p1] < rank[p2]:
                    p1, p2 = p2, p1
                if rank[p1] == rank[p2]:
                    rank[p1] += 1
                    
                parent[p2] = p1
                
                
            
        for i in range(1, n + 1):
            curr_dislikes = dislike[i]
            curr_parent = find(i)
            union_with = -1

            for j in range(len(curr_dislikes)):
                if find(curr_dislikes[j]) == curr_parent:
                    return False
                
                if union_with == -1:
                    union_with = curr_dislikes[j]
                    continue
                
                
                union(union_with, curr_dislikes[j])
                
        
        
        
        return True
                
        
            
            
            
        
        