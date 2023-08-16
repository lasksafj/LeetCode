class Solution {
public:
    long long appealSum(string s) {
        unordered_map<char,int> prev;
        vector<int> dp(s.size());
        dp[0] = 1;
        prev[s[0]] = 0;
        for (int i = 1; i < s.size(); i++) {
            if (prev.find(s[i]) == prev.end()) {
                prev[s[i]] = -1;
            }
            dp[i] = dp[i-1] + i - prev[s[i]];
            prev[s[i]] = i;
        }
        long long res = 0;
        for (int n: dp) {
            res += n;
        }
        return res;
    }
};