class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free,have,cool = 0,-inf,-inf
        for p in prices:
            free_d,have_d,cool_d = free,have,cool
            free = max(free_d, cool_d)
            have = max(have_d, free_d - p)
            cool = max(cool_d, have_d + p)
        return max(free,cool)