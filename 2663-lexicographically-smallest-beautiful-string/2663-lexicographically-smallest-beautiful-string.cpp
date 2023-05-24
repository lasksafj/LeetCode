class Solution {
public: 
    string smallestBeautifulString(string s, int k) {
        char ma = (int)'a' + k, mi = 'a';
        int n = s.size();
        for (int i = n-1; i >= 0; i--) {
            s[i]++;
            if (s[i] < ma) {
                if ((i-1 >= 0 && s[i] == s[i-1]) || (i-2 >= 0 && s[i] == s[i-2])) {
                    i++;
                }
                else {
                    for (int j = i+1; j < n; j++) {
                        s[j] = 'a';
                        while (s[j] == s[j-1] || (j-2>=0 && s[j]==s[j-2])) {
                            s[j]++;
                        }
                    }
                    return s;
                }
                    
            }
        }
        return "";
    }
};