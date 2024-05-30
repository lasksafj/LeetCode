class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for k in range(len(arr)):
            mp = defaultdict(int)
            l,r = 0,0
            for i in range(k-1,-1,-1):
                l ^= arr[i]
                mp[l] += 1
            for i in range(k, len(arr)):
                r ^= arr[i]
                res += mp[r]
        return res