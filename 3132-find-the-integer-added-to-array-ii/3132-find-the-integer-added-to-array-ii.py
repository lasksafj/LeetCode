class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        s1 = sum(nums1)
        s2 = sum(nums2)
        for i in range(len(nums1)):
            for j in range(i):
                a,b = nums1[i],nums1[j]
                d = s1-(a+b)-s2
                if d%(len(nums2)) == 0:
                    x = -d // len(nums2)
                    k2 = 0
                    ok = True
                    for k1 in range(len(nums1)):
                        if k1 == i or k1 == j:
                            continue
                        if nums1[k1]+x == nums2[k2]:
                            k2 += 1
                        else:
                            ok = False
                    if ok:
                        return x
        return -1