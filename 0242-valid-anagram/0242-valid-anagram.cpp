class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        int m[27] = {0};
        for (int i = 0; i < s.size(); i++) {
            m[s[i]-'a']++;
            m[t[i]-'a']--;
        }
        for (int c : m) {
            if (c != 0)
                return false;
        }
        return true;
    }
};