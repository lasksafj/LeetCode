class Solution {
public:
    int sol(string& answerKey, int k, char ch) {
        // unordered_map<char, int> m;
        int j = 0;
        int res = 0;
        for (int i = 0; i < answerKey.size(); i++) {
            // m[answerKey[i]] += 1;
            if (answerKey[i] != ch)
                k--;
            while (j < i && k < 0) {
                if (answerKey[j] != ch) {
                    k++;
                }
                j += 1;
            }
            res = max(res, i-j+1);
        }
        return res;
    }
    
    int maxConsecutiveAnswers(string answerKey, int k) {
        return max(sol(answerKey, k, 'T'), sol(answerKey, k, 'F'));
    }
};