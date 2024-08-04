class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # counter no of subarr sum <= target, sum of sum of those subarr
        def count_sum(target):
            cur = 0
            window_s = 0
            j = 0
            cnt = 0
            res = 0
            for i in range(n):
                cur += nums[i]
                window_s += nums[i]*(i-j+1)
                while cur > target:
                    window_s -= cur
                    cur -= nums[j]
                    j += 1
                cnt += i-j+1
                res += window_s
            return (cnt,res)
        
        # sum of all elem until index k in new array.
        def sol(k):
            l,r = 0, sum(nums)
            while l <= r:
                mi = (l+r)//2
                cnt,s = count_sum(mi)
                if cnt >= k:
                    r = mi-1
                else:
                    l = mi+1
            cnt,s = count_sum(l)
            return s - l*(cnt-k)
        return (sol(right) - sol(left-1)) % (10**9+7)