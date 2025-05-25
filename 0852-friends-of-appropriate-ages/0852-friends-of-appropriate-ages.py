class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        for i,x in enumerate(ages):
            # 0.5*x+7 < y <= x
            l = floor(0.5*x+7 + 1)
            r = x
            a = bisect_left(ages, l)
            b = bisect_right(ages, r)
            res += max(0, b-a - 1)
        return res