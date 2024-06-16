class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        # change elem in big_nums to position of bit of that elem -> [0, 1, 0,1, 2, 0,2,...]
        # ans = product = sum of all such positions
        
        def count(x):
            # sum of set bit for all number in [1,x)
            # for number power of 2, ex: 1,2,4,8,16
            #   x = 1<<i
            #   count(x) = i * 2^(i-1)
            if x == 0:
                return 0
            i = x.bit_length()-1
            v = 1<<i
            return i * (v>>1) + count(x-v) + x-v
        
        def sum_pos(x):
            # sum of all position of set bit for all number in [1,x)
            if x == 0:
                return 0
            i = x.bit_length()-1
            v = 1<<i
            return (v>>1) * i*(i-1)//2 + sum_pos(x-v) + (x-v)*i
        
        def query(k):
            if k == 0:
                return 0
            # find largest x such that count(x) <= k
            x = bisect_right(range(10**15), k, key=count) - 1
            res = sum_pos(x)
            k -= count(x)
            
            # find sum of all remaining set bit position
            for _ in range(k+1):
                b = x&(-x)
                res += b.bit_length()-1
                x -= b
            return res
        
        res = []
        for a,b,m in queries:
            res.append(pow(2, query(b) - (query(a-1) if a>0 else 0), m))
        return res