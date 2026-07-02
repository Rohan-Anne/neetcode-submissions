import heapq
class Twitter:

    def __init__(self):
        self.mapping = dict()
        for i in range(1, 101):
            tweets = set()
            followees = set()
            followees.add(i)
            self.mapping[i] = [followees, tweets]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.mapping[userId][1].add((self.time, -tweetId))
        self.time -= 1
        print("Tweet posted!")
            
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []
        # Aggregate all followed tweets
        for followee in self.mapping[userId][0]:
            for tweet in self.mapping[followee][1]:
                heapq.heappush(heap, tweet)
        print(heap)
        for i in range(10):
            if len(heap) > 0:
                feed.append(-1 * heapq.heappop(heap)[1])
        return feed
        print("Feed retrieved!")

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.mapping[followerId][0]:
            return None # Already following
        self.mapping[followerId][0].add(followeeId)
        print("User followed!")

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return None # You can't unfollow yourself
        if followeeId not in self.mapping[followerId][0]:
            return None # Already not following
        self.mapping[followerId][0].remove(followeeId)
        print("User unfollowed!")
        
