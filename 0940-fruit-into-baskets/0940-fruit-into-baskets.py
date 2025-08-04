class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m = defaultdict(int)
        res = 0
        j = 0
        for i in range(len(fruits)):
            m[fruits[i]] += 1
            while j < i and len(m) > 2:
                m[fruits[j]] -= 1
                if m[fruits[j]] == 0:
                    del m[fruits[j]]
                j += 1
            res = max(res, i-j+1)
        return res