class Leaderboard:

    def __init__(self):
        self.mp = defaultdict(int)
        self.A = SortedList([], key=lambda x: self.mp[x])

    def addScore(self, playerId: int, score: int) -> None:
        self.A.discard(playerId)
        self.mp[playerId] += score
        self.A.add(playerId)

    def top(self, K: int) -> int:
        return sum(self.mp[p] for p in self.A[-K:])

    def reset(self, playerId: int) -> None:
        self.A.discard(playerId)
        self.mp[playerId] = 0
        self.A.add(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)