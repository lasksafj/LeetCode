class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(k):
            if k == 1:
                return 0
            i = ceil(log2(k))-1
            if k&(k-1) == 0:
                k >>= 1
            else:
                k -= 1<<int(log2(k))
            n = dfs(k)
            return n + operations[i]
        return chr(dfs(k)%26 + 97)