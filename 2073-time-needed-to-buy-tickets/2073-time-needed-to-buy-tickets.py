class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([i for i in range(len(tickets))])
        time = 0
        while queue:
            person = queue.popleft()
            
            time += 1
            tickets[person] -= 1
            
            if tickets[person] > 0:
                queue.append(person)
            
            elif person == k and tickets[person] == 0:
                return time
                
            
            
         