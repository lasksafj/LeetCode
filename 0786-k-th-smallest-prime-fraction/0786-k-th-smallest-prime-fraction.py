class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        l,r = 0,1
        while l < r:
            mi = (l+r)/2
            res1,res2 = 0,0
            total_smaller_fractions = 0
            max_fraction = 0
            j = 1
            for i in range(N-1):
                while j < N and arr[i] >= arr[j] * mi:
                    j += 1
                total_smaller_fractions += N-j
                if j == N:
                    break
                if arr[i]/arr[j] > max_fraction:
                    res1,res2 = i,j
                    max_fraction = arr[i]/arr[j]
                    
            if total_smaller_fractions > k:
                r = mi
            elif total_smaller_fractions < k:
                l = mi
            else:
                return arr[res1],arr[res2]
        return []