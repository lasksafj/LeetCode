class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:        
        # Corrected Slope Normalizer
        def f(dy, dx):
            if dx == 0: return (1, 0) # Canonical vertical
            if dy == 0: return (0, 1) # Canonical horizontal
            
            d = gcd(dy, dx)
            dy //= d
            dx //= d
            
            # Ensure the denominator (dx) is always positive
            if dx < 0:
                dy, dx = -dy, -dx
            return dy, dx

        N = len(points)
        mp = defaultdict(lambda: defaultdict(int))
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                
                # Get canonical slope
                slope = f(y2 - y1, x2 - x1)
                
                # Calculate Intercept
                # Using cross-multiplication logic to avoid floats
                # For line: dy*x - dx*y + C = 0
                # "Intercept" identifier can be: dy*x - dx*y
                # Note: We must use the canonical slope (dy, dx) here
                dy_s, dx_s = slope
                b = dy_s * x2 - dx_s * y2
                
                mp[slope][b] += 1
                
        res = 0
        
        # 1. Add counts for parallel segments (same slope, different intercept)
        for slope, intercepts in mp.items():
            current_sum = 0
            total_seen = 0
            for count in intercepts.values():
                current_sum += total_seen * count
                total_seen += count
            res += current_sum

        # 2. Subtract counts for segments sharing a midpoint (Parallelograms)
        mid_cnt = defaultdict(lambda: defaultdict(int))
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                mid = (x1 + x2, y1 + y2)
                slope = f(y2 - y1, x2 - x1)
                mid_cnt[mid][slope] += 1
                
        for slope_counts in mid_cnt.values():
            current_sum = 0
            total_seen = 0
            for count in slope_counts.values():
                current_sum += total_seen * count
                total_seen += count
            res -= current_sum
            
        return res