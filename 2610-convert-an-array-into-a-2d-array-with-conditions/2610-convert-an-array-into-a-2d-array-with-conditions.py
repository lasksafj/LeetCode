class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = Counter(nums)
        res = []
        while len(m) > 0:
            a = []
            b = list(m.keys())
            for e in b:
                if m[e] > 0:
                    a.append(e)
                    m[e] -= 1
                if m[e] == 0:
                    del m[e]
            res.append(a)
        return res