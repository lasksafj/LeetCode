class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        N = len(arr)
        res = set()
        s = {0} # all unique OR of subarr ending at j, len of this <= 32, b/c OR arr[i,j] >= arr[i+1,j]
        for n in arr:
            s = {a | n for a in s} | {n}
            res |= s
        return len(res)