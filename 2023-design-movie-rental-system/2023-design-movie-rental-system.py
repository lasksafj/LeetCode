class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.P = defaultdict(int)
        self.M = defaultdict(lambda: SortedList())
        self.R = SortedList([], key=lambda e: [self.P[e], e[0], e[1]] )
        for s,m,p in entries:
            self.P[(s,m)] = p
            self.M[m].add((p,s))

    def search(self, movie: int) -> List[int]:
        return [s for p,s in self.M[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        self.R.add((shop, movie))
        p = self.P[(shop, movie)]
        self.M[movie].remove((p, shop))

    def drop(self, shop: int, movie: int) -> None:
        self.R.remove((shop, movie))
        p = self.P[(shop, movie)]
        self.M[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        return self.R[:5]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()