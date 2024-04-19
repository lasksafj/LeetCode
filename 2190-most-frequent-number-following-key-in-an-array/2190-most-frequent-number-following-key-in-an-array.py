class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = defaultdict(int)
        for a,b in zip(nums,nums[1:]):
            if a == key:
                cnt[b] += 1
        return max(cnt, key=lambda x:cnt[x])