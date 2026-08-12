class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        mp = defaultdict(int)
        fq = defaultdict(int)
        mf = 0
        j = 0
        for i in range(len(nums)):
            fq[mp[nums[i]]] -= 1
            mp[nums[i]] += 1
            fq[mp[nums[i]]] += 1
            mf = max(mf, mp[nums[i]])
            while j < i and mf > k:
                if mf == mp[nums[j]] and fq[mp[nums[j]]] == 1:
                    mf -= 1
                fq[mp[nums[j]]] -= 1
                mp[nums[j]] -= 1
                fq[mp[nums[j]]] += 1
                j += 1
            res = max(res, i-j+1)
        return res