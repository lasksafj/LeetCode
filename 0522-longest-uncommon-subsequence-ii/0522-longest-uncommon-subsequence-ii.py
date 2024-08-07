class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def issubseq(s1, s2):
            i = 0
            for c in s1:
                while i < len(s2) and s2[i] != c:
                    i += 1
                if i == len(s2):
                    return False
                i += 1
            return True
        A = sorted(strs, key=len, reverse=True)
        for i,s1 in enumerate(A):
            if all(not issubseq(s1, s2) for j,s2 in enumerate(A) if i!=j):
                return len(s1)
        return -1