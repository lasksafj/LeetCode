class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums = [-inf] + nums + [inf]
        N = len(nums)
        sl = SortedList()
        L = [-1] + list(range(N-1))
        R = list(range(1, N+1))
        inv = 0
        for i in range(1, N-2):
            if nums[i] > nums[i+1]:
                inv += 1
            sl.add( [nums[i]+nums[i+1], i, i+1] )
        res = 0
        while inv:
            c,i,j = sl.pop(0)
            l,r = L[i], R[j]
            if nums[i] > nums[j]:
                inv -= 1
            if nums[l] > nums[i] and nums[l] <= c:
                inv -= 1
            if nums[l] <= nums[i] and nums[l] > c:
                inv += 1
            if nums[j] > nums[r] and c <= nums[r]:
                inv -= 1
            if nums[j] <= nums[r] and c > nums[r]:
                inv += 1
            if l:
                sl.remove( [nums[l]+nums[i], l, i] )
                sl.add( [nums[l]+c, l, i] )
            if r < N-1:
                sl.remove( [nums[j]+nums[r], j, r] )
                sl.add( [c+nums[r], i, r] )
            nums[i] = c
            R[i] = r
            L[r] = i
            res += 1
        return res