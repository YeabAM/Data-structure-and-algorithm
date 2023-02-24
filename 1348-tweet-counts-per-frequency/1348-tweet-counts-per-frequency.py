class TweetCounts:

    def __init__(self):
        self.record = defaultdict(list)
    
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.record[tweetName].append(time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            #divide by 60
            chunk_size = ((endTime - startTime) // 60) + 1
            chunk = [0 for _ in range(chunk_size)]
            divider = 60
            # print(chunk_size, startTime, endTime)
            #iterate through tweet time fo the tweet
            for time in self.record[tweetName]:
                #for each time, if out of bound dont consider
                if startTime <= time <= endTime:
                    #find pos, divide by initial_divider + start_time
                    pos = (time - startTime) // divider
                    chunk[pos] += 1
                    
            return chunk
        
        elif freq == 'hour':
            #divide by 3600
            chunk_size = ((endTime - startTime) // 3600) + 1
            chunk = [0 for _ in range(chunk_size)]
            divider = 3600
            #iterate through tweet time fo the tweet
            for time in self.record[tweetName]:
                #for each time, if out of bound dont consider
                if startTime <= time <= endTime:
                    #find pos, divide by initial_divider + start_time
                    pos = (time - startTime) // divider
                    chunk[pos] += 1
                    
            return chunk
        
        else:
            #divide by '86400'
            chunk_size = ((endTime - startTime) // 86400) + 1
            chunk = [0 for _ in range(chunk_size)]
            divider = 86400
            #iterate through tweet time fo the tweet
            for time in self.record[tweetName]:
                #for each time, if out of bound dont consider
                if startTime <= time <= endTime:
                    #find pos, divide by initial_divider + start_time
                    pos = (time - startTime) // divider
                    chunk[pos] += 1
                    
            return chunk
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)