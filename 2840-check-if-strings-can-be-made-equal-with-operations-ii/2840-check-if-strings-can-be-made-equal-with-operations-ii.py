class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        A1 = Counter([s1[i] for i in range(len(s1)) if i&1])
        A2 = Counter([s1[i] for i in range(len(s1)) if i&1==0])
        B1 = Counter([s2[i] for i in range(len(s1)) if i&1])
        B2 = Counter([s2[i] for i in range(len(s1)) if i&1==0])
        return A1 == B1 and A2 == B2