from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(list)
        self.tweetsMap = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append((self.timestamp, tweetId))
        self.timestamp +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetHeap = []
        heapq.heapify_max(tweetHeap)
        index = len(self.tweetsMap[userId])-1
        if len(self.tweetsMap[userId]) > 0:
            heapq.heappush_max(tweetHeap, (self.tweetsMap[userId][index][0], self.tweetsMap[userId][index][1], userId, index))
        for follow in self.followingMap[userId]:
            index = len(self.tweetsMap[follow])-1
            heapq.heappush_max(tweetHeap, (self.tweetsMap[follow][index][0], self.tweetsMap[follow][index][1], follow, index))

        count = 0
        newsFeed=[]
        while count < 10 and tweetHeap:
            topTweet = heapq.heappop_max(tweetHeap)
            newsFeed.append(topTweet[1])
            newIndex = topTweet[3]-1
            follow = topTweet[2]
            if newIndex >= 0:
                heapq.heappush_max(tweetHeap, (self.tweetsMap[follow][newIndex][0], self.tweetsMap[follow][newIndex][1], follow, newIndex))
            count +=1

        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followingMap[followerId]: 
            self.followingMap[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)

