class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = defaultdict(int)
        for i,ch in enumerate(order):
            m[ch] = i
        return ''.join(sorted(s, key=lambda ch:m[ch]))