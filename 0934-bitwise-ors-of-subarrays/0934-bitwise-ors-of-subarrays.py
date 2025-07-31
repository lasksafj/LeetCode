class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        N = len(arr)
        mp = defaultdict(lambda:-1)
        for i in range(N):
            a = 0
            for j in range(i, -1, -1):
                a |= arr[j]
                if mp[a] >= j-1 and mp[a] < i:
                    mp[a] = i
                    break
                mp[a] = i
        return len(mp)