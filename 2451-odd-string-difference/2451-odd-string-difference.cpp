class Solution {
public:
    bool cmp(string& a, string& b) {
        int n = a.size();
        for (int i = 0; i < n-1; i++) {
            if (a[i+1] - a[i] != b[i+1] - b[i])
                return false;
        }
        return true;
    }
    
    string oddString(vector<string>& words) {
        int n = words[0].size();
        for (int i = 1; i < words.size()-1; i++) {
            if (!cmp(words[i], words[i-1]) && !cmp(words[i], words[i+1]))
                return words[i];
        }
        return !cmp(words[0], words[1])? words[0]: words.back();
    }
};