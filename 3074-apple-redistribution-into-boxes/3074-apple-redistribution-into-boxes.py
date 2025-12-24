class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        res = 0
        for n in sorted(capacity, reverse=True):
            s -= n
            res += 1
            if s <= 0: break
        return res