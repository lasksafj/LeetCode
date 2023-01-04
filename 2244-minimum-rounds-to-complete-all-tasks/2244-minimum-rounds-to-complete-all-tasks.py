class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        m = Counter(tasks)
        res = 0
        for k,v in m.items():
            if v == 1:
                return -1
            a,b = v%3, v//3
            if a == 0:
                res += b
            else:
                res += b+1
        return res
                