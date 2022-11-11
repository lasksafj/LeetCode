class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0, j=0, n = nums.size();
        for  (int j = 1; j < n; j++) {
            while (j < n && nums[j] == nums[j-1]) {
                j++;
            }
            if (j < n)
                nums[++i] = nums[j];
        }
        return i+1;
    }
};