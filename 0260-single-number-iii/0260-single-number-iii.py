class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXorb = 0
        for n in nums:
            aXorb ^= n
        d = aXorb & (-aXorb) # least significant bit in aXorb, the bit that a differs from b
        # divide all number into 2 groups: 1 has bit d, 2 does not
        gr1,gr2 = 0,0
        for n in nums:
            if n & d:
                gr1 ^= n
            else:
                gr2 ^= n
        return [gr1,gr2]