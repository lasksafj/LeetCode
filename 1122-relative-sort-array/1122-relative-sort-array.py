class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {}
        for i,n in enumerate(arr2):
            mp[n] = i
        return sorted(arr1, key=lambda n: mp[n] if n in mp else n+len(arr2)) 