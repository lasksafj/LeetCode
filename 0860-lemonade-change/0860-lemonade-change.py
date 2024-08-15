class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = defaultdict(int)
        no5 = 0
        for b in bills:
            mp[b] += 1
            change = b-5
            for x in [20,10,5]:
                mi = min(mp[x], change//x)
                change -= mi * x
                mp[x] -= mi
            if change > 0:
                return False
        return True