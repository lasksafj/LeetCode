class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = -2
        flowerbed.extend([0,1])
        for i,v in enumerate(flowerbed):
            if v == 1:
                l = max(0, i-prev-2)
                n -= l//2
                prev = i
        return n <= 0