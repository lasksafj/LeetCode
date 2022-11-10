class Solution {
public:
    int destroyTargets(vector<int>& nums, int space) {
        unordered_map<int,int> m;
        int ma = 0, res = INT_MAX;
        for (int n : nums) {
            ma = max(ma, ++m[n%space]);
        }
        for (int n : nums) {
            if (m[n%space] == ma)
                res = min(res, n);
        }
        return res;
        
    }
};