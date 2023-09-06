class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.L = int(log2(n)) + 2
        self.up = [[-1]*self.L for _ in range(n)]
        for i in range(self.L):
            for j in range(n):
                if i == 0:
                    self.up[j][i] = parent[j]
                elif self.up[j][i-1] != -1:
                    self.up[j][i] = self.up[self.up[j][i-1]][i-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.L-1,-1,-1):
            if k&(1<<i):
                node = self.up[node][i]
                if node == -1:
                    return node
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)