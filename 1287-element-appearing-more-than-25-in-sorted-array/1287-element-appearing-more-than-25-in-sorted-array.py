class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        m = Counter(arr)
        for x,y in m.items():
            if y > len(arr)//4:
                return x
        return -1