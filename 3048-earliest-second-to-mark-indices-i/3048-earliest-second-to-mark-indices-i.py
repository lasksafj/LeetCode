class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def check(x):
            last_idx, last = set(),set()
            for i in range(x-1,-1,-1):
                if changeIndices[i] not in last:
                    last_idx.add(i)
                    last.add(changeIndices[i])
            if len(last_idx) < len(nums):
                return False
            minus1 = 0
            for i in range(x):
                if i in last_idx:
                    if minus1 >= nums[changeIndices[i]-1]:
                        minus1 -= nums[changeIndices[i]-1]
                    else:
                        return False
                else:
                    minus1 += 1
            return True
            
        l,r = 0, len(changeIndices)
        res = -1
        while l <= r:
            mi = (l+r)//2
            if check(mi):
                r = mi-1
                res = mi
            else:
                l = mi+1
        return res