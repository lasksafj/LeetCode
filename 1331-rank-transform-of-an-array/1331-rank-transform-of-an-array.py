class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        A = sorted(set(arr))
        mp = {a:i+1 for i,a in enumerate(A)}
        return [mp[a] for a in arr]