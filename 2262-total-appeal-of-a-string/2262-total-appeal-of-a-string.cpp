class Solution {
public:
    long long appealSum(string s) {
        unordered_map<char,int> prev;
        vector<int> dp(2);
        dp[0] = 1;
        long long res = 1;
        prev[s[0]] = 0;
        for (int i = 1; i < s.size(); i++) {
            if (prev.find(s[i]) == prev.end()) {
                prev[s[i]] = -1;
            }
            dp[i%2] = dp[(i-1)%2] + i - prev[s[i]];
            prev[s[i]] = i;
            res += dp[i%2];
        }
        return res;
    }
};