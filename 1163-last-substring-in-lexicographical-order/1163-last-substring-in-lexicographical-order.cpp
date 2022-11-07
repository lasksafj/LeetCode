class Solution {
public:
    string lastSubstring(string s) {
        char ma = 'A';
        int midx = s.size() - 1;
        for (int i = s.size()-1; i >= 0; i--) {
            if (ma < s[i]) {
                midx = i;
                ma = s[i];
            }
            else if (ma == s[i]) {
                int j = i+1,
                    jm = midx + 1;
                while (j < midx && jm < s.size()) {
                    if (s[j] < s[jm])
                        break;
                    else if (s[j] > s[jm])
                        j = midx-1;
                    j++;
                    jm++;
                }
                if (j == midx || jm == s.size())
                    midx = i;
            }
        }
        return s.substr(midx);
    }
};