class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int s = 0;
        for (int n : nums) {
            s += n;
        }
        return nums.size() * (nums.size()+1)/2 - s;
    }
};