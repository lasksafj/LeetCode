class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # print()
        cnt = Counter(nums)
        end = defaultdict(int)
        for n in nums:
            if cnt[n] == 0:
                continue
            cnt[n] -= 1
            if end[n-1] > 0:
                end[n-1] -= 1
                end[n] += 1
            elif cnt[n+1] > 0 and cnt[n+2] > 0:
                cnt[n+1] -= 1
                cnt[n+2] -= 1
                end[n+2] += 1
            else:
                return False
            
        return True