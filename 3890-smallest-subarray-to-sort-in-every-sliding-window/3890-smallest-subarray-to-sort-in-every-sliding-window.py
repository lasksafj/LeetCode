class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        
        N = len(nums)
        def sol(nums):
            st = deque()
            nxt = [N]*N
            for i in range(N):
                while st and nums[st[-1]] <= nums[i]:
                    j = st.pop()
                    nxt[j] = i
                st.append(i)
            # a....ma..b..end...c
            # b.....c : sorted suffix
            # ma: max a......b
            # => end: last index so that nums[end] < ma
            # => ma <= nums[end+1]
            b = 0
            for i in range(k-2):
                if nums[i] > nums[i+1]:
                    b = i+1
            ma = 0
            end = [0]*(N-k+1)
            for a in range(N-k+1):
                ma = max(ma, a)
                c = a+k-1
                if nums[c-1] > nums[c]:
                    b = c
                while nxt[ma] < b:
                    ma = nxt[ma]
                end[a] = min(nxt[ma]-1, c)
            return end
        end = sol(nums)
        start = [N-n-1 for n in sol([-n for n in nums][::-1])[::-1]]
        return [end[i]-start[i]+1 if end[i] > start[i] else 0 for i in range(N-k+1)]