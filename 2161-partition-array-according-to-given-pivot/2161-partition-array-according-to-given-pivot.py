class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        A,B,C = [],[],[]
        for n in nums:
            if n < pivot:
                A.append(n)
            elif n == pivot:
                B.append(n)
            else:
                C.append(n)
        return A+B+C