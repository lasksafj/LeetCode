class Solution {
public:
    string baseNeg2(int n) {
        string res;
        while (n != 0) {
            int rem = n % -2;
            n /= -2;
            if (rem < 0) {
                rem += 2;
                n++;
            }
            res = to_string(rem) + res;
        }
        return res == ""? "0" : res;
    }
};