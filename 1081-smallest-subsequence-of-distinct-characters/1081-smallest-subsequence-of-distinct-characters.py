class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i,c in enumerate(s):
            last[c] = i
        st = []
        S = set()
        for i,c in enumerate(s):
            while st and c not in S and st[-1] > c and last[st[-1]] > i:
                S.remove(st[-1])
                st.pop()
            if c not in S:
                st.append(c)
                S.add(c)
        return ''.join(st)