class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
        # b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
        # a == b => a ^ b = 0
        # => arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0
        # => xor(arr[i:k+1]) = 0 for all j, i < j <= k
        # => number of triplet = k-i-1
        N = len(arr)
        prexor = [0]*(N+1)
        for i,n in enumerate(arr):
            prexor[i+1] = prexor[i] ^ arr[i]
        res = 0
        cnt,total_no_idx = defaultdict(int),defaultdict(int)
        cnt[0] = 1
        cur = 0
        for i in range(N):
            cur ^= arr[i]
            res += i * cnt[cur] - total_no_idx[cur]
            cnt[cur] += 1
            total_no_idx[cur] += i+1
        return res