class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        A1 = [s1[i] for i in range(len(s1)) if i&1]
        A2 = [s1[i] for i in range(len(s1)) if i&1==0]
        B1 = [s2[i] for i in range(len(s1)) if i&1]
        B2 = [s2[i] for i in range(len(s1)) if i&1==0]
        return sorted(A1)+sorted(A2) == sorted(B1)+sorted(B2)