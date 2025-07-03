class Solution:
    def kthCharacter(self, k: int) -> str:
        def dfs(k):
            if k&(k-1) == 0:
                print(k, len(bin(k))-3)
                return len(bin(k))-3
            k -= (1<<(len(bin(k)) - 3))
            return dfs(k) + 1
        return chr(dfs(k) + 97)