class Solution {
    public int jump(int[] nums) {
        int L = nums.length; // length of input array
        if (L == 1)
            return 0;
        int[] dp = new int [L]; // array dp 
        Arrays.fill(dp,Integer.MAX_VALUE); // initialize dp 
        dp[0] = 0; // initialize dp[0]
//        for(int j = 1; j <= nums[0] && j < L;j++) 
//            dp[j] = 1;
//        int max_r = nums[0];
        dp[1] = 1;
        int max_r = 0;
        for(int i = 0; i <= L - 1; i++) {
            
            int r1 = i + nums[i];
            
            if(r1 > max_r){
                for(int k = max_r + 1; k <= r1 && k < L; k++)
                    dp[k] = dp[i] + 1;
            }
            if(max_r < i + nums[i])
                max_r = i + nums[i];
            // System.out.println(dp[i]);
        }
        
        return dp[L-1];
    }
}