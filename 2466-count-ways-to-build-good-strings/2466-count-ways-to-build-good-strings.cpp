class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        int mod = 1000000007;
        long dp[100001][2];
        memset(dp, 0, sizeof(dp));
        dp[one][1] = 1;
        dp[zero][0] = 1;
        for (int i = 0; i <= high; i++) {
            if (i - zero > 0)
                dp[i][0] = (dp[i-zero][0] + dp[i-zero][1]) % mod;
            if (i - one > 0)
                dp[i][1] = (dp[i-one][0] + dp[i-one][1]) % mod;
        }
        long res = 0;
        for (int i = low; i <= high; i++) {
            res = (res + dp[i][0] + dp[i][1]) % mod;
        }
        return res % mod;
    }
};