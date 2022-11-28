class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # A = [0]*n
        # j = 0
        # for i in range(n):
        #     if nums[i] > k:
        #         A[i] = 1
        #     elif nums[i] < k:
        #         A[i] = -1
        #     else:
        #         A[i] = 0
        #         j = i
        # for i in range(j,-1,-1):
        #     left[]
        res = 0
        left = defaultdict(int)
        for i in range(n):
            if nums[i] == k:
                a,b = i,i
                largers,smallers = 0,0
                while a >= 0:
                    if nums[a] > k:
                        largers += 1
                    elif nums[a] < k:
                        smallers += 1
                    left[largers-smallers] += 1
                    a -= 1
                # print(left)
                largers,smallers = 0,0
                while b < n:
                    if nums[b] > k:
                        largers += 1
                    elif nums[b] < k:
                        smallers += 1
                    res += left[smallers-largers] + left[smallers-largers+1]
                    b += 1
                return res
        return res
                
            