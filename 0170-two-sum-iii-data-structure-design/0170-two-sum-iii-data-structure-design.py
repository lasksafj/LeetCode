class TwoSum:

    def __init__(self):
        self.mp = defaultdict(int)

    def add(self, number: int) -> None:
        self.mp[number] += 1

    def find(self, value: int) -> bool:
        for a in self.mp:
            b = value - a
            if b in self.mp and (b != a or self.mp[b] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)