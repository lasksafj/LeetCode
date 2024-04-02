from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        A = [nums[0]]
        B = [nums[1]]
        sortedA = SortedList([nums[0]])
        sortedB = SortedList([nums[1]])
        for n in nums[2:]:
            p1 = len(sortedA) - sortedA.bisect_right(n)
            p2 = len(sortedB) - sortedB.bisect_right(n)
            if p1 > p2:
                A.append(n)
                sortedA.add(n)
            elif p1 < p2:
                B.append(n)
                sortedB.add(n)
            else:
                if len(A) <= len(B):
                    A.append(n)
                    sortedA.add(n)
                else:
                    B.append(n)
                    sortedB.add(n)
        return A + B