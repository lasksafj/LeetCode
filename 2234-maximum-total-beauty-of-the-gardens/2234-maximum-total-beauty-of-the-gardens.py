class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        len_flowers = len(flowers)
        no_full = 0
        for i in range(len_flowers-1,-1,-1):
            if flowers[i] >= target:
                no_full += 1
        if no_full == len_flowers:
            return full*len_flowers
        pre = [0]*len_flowers
        pre[0] = flowers[0]
        for i in range(1,len_flowers):
            pre[i] = pre[i-1] + flowers[i]
        # print(flowers,pre,no_full)
        def check(x):
            right = len_flowers-no_full-1
            if len_flowers*full >= x and target*(right+1) - pre[right] <= newFlowers:
                return True
            
            for comp in range(no_full, len_flowers):
                left = len_flowers-comp
                remain_flowers = newFlowers - (target*(right-left+1) - (pre[right] - pre[left-1]))
                if remain_flowers < 0:
                    return False
                mi = ceil((x-comp*full)/partial)
                if mi < target:
                    p = bisect_right(flowers, mi)
                    p = min(p, left)
                    if p == 0:
                        return True
                    if mi*p - pre[p-1] <= remain_flowers:
                        return True
            return False
            
        l,r = 0, full*len_flowers+(flowers[-1]+newFlowers)*partial
        # print(r)
        while l <= r:
            m = (l+r)//2
            # print(l,m,r)
            if check(m):
                l = m+1
            else:
                r = m-1
        return r