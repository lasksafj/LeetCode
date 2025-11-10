class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        res = 0
        for n in nums + [0]:
            while st and st[-1] > n:
                st.pop()
                res += 1
            if not st or st[-1] < n:
                st.append(n)
        return res