class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            L,M,R = [],[],[]
            for n in nums:
                if n > pivot:
                    R.append(n)
                elif n < pivot:
                    L.append(n)
                else:
                    M.append(n)
            if k <= len(R):
                return quick_select(R, k)
            if len(R) + len(M) < k:
                return quick_select(L, k - len(M) - len(R))
            return pivot
        return quick_select(nums, k)