class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        N = len(nums)
        st = []
        for n in nums:
            st.append(n)
            while len(st) >= 2 and gcd(st[-1], st[-2]) > 1:
                st[-2] = lcm(st[-1], st[-2])
                st.pop()
            
        return st