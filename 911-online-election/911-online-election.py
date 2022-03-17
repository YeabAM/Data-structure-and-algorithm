class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        self.times = times
        counts = defaultdict(int)
        maxCount = 0
        for i in range(len(times)):
            counts[persons[i]] += 1 
            if counts[persons[i]] > maxCount:
                maxCount += 1
                currLeader = [persons[i]]
            elif counts[persons[i]] == maxCount:
                currLeader.append(persons[i])
            self.leaders.append(currLeader[-1])
        

    def q(self, t: int) -> int:
        index = bisect.bisect_left(self.times , t)
        # print(self.leaders)
        if index == len(self.times) or self.times[index] > t:
            
            return self.leaders[index - 1]
        return self.leaders[index]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)