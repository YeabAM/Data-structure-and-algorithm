class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))
            
        # print(self.newfeed)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweet[userId].copy()
        # print(tweets,'before')
        for follows in self.follows[userId]:
            
            tweets += self.tweet[follows]
            
        # print(tweets)
        
        tweets.sort(key = lambda x: -x[0])
        
        most_recent = [tweet for time, tweet in tweets[:10]]
        
        return most_recent
            
        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)