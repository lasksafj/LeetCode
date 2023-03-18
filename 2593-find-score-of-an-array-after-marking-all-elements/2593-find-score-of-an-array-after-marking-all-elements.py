class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = []
        for i,n in enumerate(nums):
            heappush(pq, [n,i])
        m = defaultdict(bool)
        res = 0
        while pq:
            v,i = heappop(pq)
            if i not in m:
                res += v
                m[i],m[i+1],m[i-1] = True,True,True
        return res