class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rate = {}
        self.cuisine = {}
        self.SL = defaultdict(lambda: SortedList([], key=lambda x:[-self.rate[x], x]))
        for f,c,r in zip(foods,cuisines,ratings):
            self.rate[f] = r
            self.SL[c].add(f)
            self.cuisine[f] = c

    def changeRating(self, food: str, newRating: int) -> None:
        self.SL[self.cuisine[food]].remove(food)
        self.rate[food] = newRating
        self.SL[self.cuisine[food]].add(food)

    def highestRated(self, cuisine: str) -> str:
        return self.SL[cuisine][0]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)