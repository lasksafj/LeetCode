class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0
        mil,mir = 0,0
        while l < r:
            if height[l] < height[r]:
                res += max(0, mil - height[l])
                mil = max( mil, height[l])
                l += 1
            else:
                res += max(0, mir - height[r])
                mir = max(mir, height[r])
                r -= 1
        return res