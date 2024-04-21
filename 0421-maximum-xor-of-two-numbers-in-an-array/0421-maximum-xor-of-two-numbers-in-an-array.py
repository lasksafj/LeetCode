class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0
        for i in range(31,-1,-1):
            mask |= 1<<i
            s = set()
            res = res|(1<<i)
            ok = False
            for n in nums:
                if res^n & mask in s:
                    ok = True
                    break
                s.add(n&mask)
            if not ok:
                res = res&~(1<<i)
        return res