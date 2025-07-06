class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        x = self.nums2[index]
        self.nums2[index] += val
        self.cnt2[x] -= 1
        self.cnt2[x+val] += 1

    def count(self, tot: int) -> int:
        res = 0
        for a,b in self.cnt1.items():
            res += b * self.cnt2[tot-a]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)