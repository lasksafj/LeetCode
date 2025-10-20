class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for s in operations:
            if s[0] == '+' or s[-1] == '+':
                res += 1
            else:
                res -= 1
        return res