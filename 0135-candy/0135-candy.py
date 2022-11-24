class Solution:
    def candy(self, ratings: List[int]) -> int:
        dist = [1 for _ in range(len(ratings))]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dist[i] = dist[i-1] + 1
            # else:
            #     dist[i] = dist[i-1] + 1
        
        # print(dist)
        for i in range(len(ratings) -2, -1, -1):
            if ratings[i] > ratings[i+1] and dist[i] <= dist[i+1]:
                dist[i] = dist[i+1] + 1
                
        # print(dist)
                
        return sum(dist)
                
        
        