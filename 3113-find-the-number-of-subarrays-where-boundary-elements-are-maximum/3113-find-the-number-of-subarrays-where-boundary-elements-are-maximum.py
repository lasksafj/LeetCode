class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        nums.append(inf)
        st = []
        res = 0
        for n in nums:
            while st and st[-1] < n:
                a = st.pop()
                no_equal = 1
                while st and st[-1] == a:
                    st.pop()
                    no_equal += 1
                res += (no_equal+1)*no_equal//2
            st.append(n)
        return res