class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr)
        while l <= r:
            m = (l+r)//2
            if arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m-1
        return l