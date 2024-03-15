class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        first,first_idx = set(),set()
        for i,idx in enumerate(changeIndices):
            if nums[idx-1] and idx not in first:
                first_idx.add(i)
                first.add(idx)

        def check(x):
            # numbers which are marked
            pq = []
            mark = 0
            for i in range(x-1,-1,-1):
                if i in first_idx:
                    n = nums[changeIndices[i]-1]
                    heappush(pq, n)
                    if mark:
                        mark -= 1
                    else:
                        mark += 1
                        heappop(pq)
                else:
                    mark += 1
            return sum(nums) + len(nums) - sum(pq) - len(pq) <= mark
        
        l,r = 0,len(changeIndices)+1
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
            else:
                l = mi+1
        return l if l <= len(changeIndices) else -1