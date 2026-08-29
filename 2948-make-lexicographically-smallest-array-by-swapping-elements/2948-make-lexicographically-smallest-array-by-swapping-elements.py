class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        A = sorted([n,i] for i,n in enumerate(nums))
        grps = []
        i = 0
        while i < N:
            j = i+1
            grp = [A[i]]
            while j < N and A[j][0] - A[j-1][0] <= limit:
                grp.append(A[j])
                j += 1            
            grps.append(grp)
            i = j
        res = [0]*N
        for grp in grps:
            I = []
            for _,i in grp:
                I.append(i)
            j = 0
            for i in sorted(I):
                res[i] = grp[j][0]
                j += 1
        return res