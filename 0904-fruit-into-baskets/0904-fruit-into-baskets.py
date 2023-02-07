class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        j = 0
        s,res = 0,0
        l = 0
        m = defaultdict(int)
        for i in range(n):
            s += 1
            m[fruits[i]] += 1
            if m[fruits[i]] == 1:
                l += 1
            while j <= i and l > 2:
                m[fruits[j]] -= 1
                if m[fruits[j]] == 0:
                    l -= 1
                s -= 1
                j += 1
            res = max(res, s)
        return res