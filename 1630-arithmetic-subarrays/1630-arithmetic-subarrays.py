class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for a,b in zip(l,r):
            if a==b:
                res.append(False)
                continue
                
            A = nums[a:b+1]
            mi,ma = min(A),max(A)
            if (ma-mi) % (len(A)-1) != 0:
                res.append(False)
                continue
            diff = (ma-mi) // (len(A)-1)
            A = set(A)
            check = True
            while mi < ma:
                if mi+diff not in A:
                    check = False
                    break
                mi += diff
            res.append(check)
        return res