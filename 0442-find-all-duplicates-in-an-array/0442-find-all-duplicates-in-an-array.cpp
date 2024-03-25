class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            int idxToNegate = abs(nums[i])-1;
            if (nums[idxToNegate] > 0) {
                nums[idxToNegate] *= -1;
            }
            else {
                res.push_back(abs(nums[i]));
            }
        }

        return res;
    }
    
};