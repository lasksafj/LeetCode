class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        A = ['']
        for c in s:
            if len(A[-1]) < k:
                A[-1] += c
            else:
                A.append(c)
        A[-1] += fill * max(0, (k - len(A[-1])))
        return A