class Solution {
public:
    bool enough(int m, int n, int k, int x) {
        int res = 0;
        for (int i = 1; i <= min(m,x); i++) {
            res += min(x/i, n);
        }
        return res >= k;
    }
    
    int findKthNumber(int m, int n, int k) {
        int l = 0, r = m*n;
        while (l < r) {
            int mid = (l+r)/2;
            if (enough(m, n, k, mid)) {
                r = mid;
            }
            else {
                l = mid+1;
            }
        }
        return r;
    }
};