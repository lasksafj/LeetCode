class Solution {
public:
    void merge(vector<int>& arr, int l, int m, int r) {
        int a1[m-l+1];
        int l1 = 0;
        for (int i = l; i <= m; i++) {
            a1[l1++] = arr[i];
        }
        int l2 = r+1;
        int i = l,
            i1 = 0,
            i2 = m+1;
        while (i1 < l1 && i2 < l2) {
            if (a1[i1] < arr[i2]) {
                arr[i++] = a1[i1++];
            }
            else {
                arr[i++] = arr[i2++];
            }
        }
        while (i1 < l1) {
            arr[i++] = a1[i1++];
        }
    }
    
    void mergesort(vector<int>& arr, int l, int r) {
        if (l >= r)
            return;
        int m = (l+r)/2;
        mergesort(arr, l, m);
        mergesort(arr, m+1, r);
        merge(arr, l, m, r);
    }
    
    vector<int> sortArray(vector<int>& nums) {
        mergesort(nums, 0, nums.size()-1);
        return nums;
    }
};