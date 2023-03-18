class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        def check(x, c):
            for r in ranks:
                c -= int(sqrt(x//r))
                if c <= 0:
                    return True
            return c <= 0
        
        l,r = 1,min(ranks)*pow(cars,2)
        while l <= r:
            m = (l+r)//2
            if check(m, cars):
                r = m-1
            else:
                l = m+1
        return l