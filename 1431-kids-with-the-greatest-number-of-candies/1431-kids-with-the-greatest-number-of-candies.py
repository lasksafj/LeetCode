class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        res = []
        for c in candies:
            if c+extraCandies >= ma:
                res.append(True)
            else:
                res.append(False)
        return res