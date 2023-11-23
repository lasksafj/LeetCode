class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for a,b in zip(l,r):
            if a==b:
                res.append(False)
                continue
            A = sorted(nums[a:b+1])
            check = True
            for i in range(2,len(A)):
                if A[i]-A[i-1] != A[1]-A[0]:
                    check = False
                    break
            res.append(check)
        return res