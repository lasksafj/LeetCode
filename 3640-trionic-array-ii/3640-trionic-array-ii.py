class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        pref = list(accumulate(nums, initial=0))
        L = [-inf]*len(nums)
        R = [-inf]*len(nums)
        R[0] = nums[0]
        R[1] = max(nums[0], nums[0] + nums[1])
        L[-1] = nums[-1]
        L[-2] = max(nums[-1], nums[-1] + nums[-2])
        j = 1
        for i in range(2, len(nums)):
            if (nums[i-1] - nums[i-2]) * (nums[i] - nums[i-1]) < 0:
                R[i] = nums[i]
                j = i
            else:
                R[i] = max(R[i-1], pref[i+1] - pref[j])
        j = len(nums)-2
        for i in range(len(nums)-3, -1, -1):
            if (nums[i] - nums[i+1]) * (nums[i+1] - nums[i+2]) < 0:
                L[i] = nums[i]
                j = i
            else:
                L[i] = max(L[i+1], pref[j+1] - pref[i])
        A = [0]

        res = -inf
        for i in range(1, len(nums)):
            if i == len(nums)-1 or (nums[i] - nums[i-1]) * (nums[i+1] - nums[i]) < 0:
                A.append(i)
                if len(A) >= 4 and nums[i]-nums[i-1] > 0:
                    a,b,c,d = A[-4:]
                    r = R[d]
                    l = L[a]
                    mid = pref[c+1] - pref[b]
                    res = max(res, mid + l + r)
            elif nums[i] == nums[i-1]:
                A.append(i-1)
                if len(A) >= 4 and nums[i-1]-nums[i-2] > 0:
                    a,b,c,d = A[-4:]
                    r = R[d]
                    l = L[a]
                    mid = pref[c+1] - pref[b]
                    res = max(res, mid + l + r)
                A = [i]
        return res