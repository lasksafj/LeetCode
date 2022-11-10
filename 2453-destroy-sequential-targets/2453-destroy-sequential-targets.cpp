class Solution {
public:
    int destroyTargets(vector<int>& nums, int space) {
        unordered_map<int,int> m1, m2;
        int ma = 0, res = 0;
        for (int n : nums) {
            int a = n%space;
            m1[a]++;
            if (m2.find(a) == m2.end())
                m2[a] = n;
            else
                m2[a] = min(m2[a], n);
        }
        for (auto& e : m1) {
            if (e.second > ma) {
                res = m2[e.first];
                ma = e.second;
            }
            else if (e.second == ma) {
                res = min(res, m2[e.first]);
            }
        }
        return res;
        
    }
};