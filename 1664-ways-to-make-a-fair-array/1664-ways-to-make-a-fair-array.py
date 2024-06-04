class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        even,odd = [0],[0]
        for i in range(N):
            if i%2 == 0:
                even.append(even[-1] + nums[i])
            else:
                odd.append(odd[-1] + nums[i])
        # print(even)
        # print(odd)
        res = 0
        for i in range(N):
            a = even[(i+1)//2] + odd[len(odd)-1] - odd[(i+1)//2]
            b = odd[i//2] + even[len(even)-1] - even[i//2+1]
            res += (a==b)
            # print(a,b)
        return res