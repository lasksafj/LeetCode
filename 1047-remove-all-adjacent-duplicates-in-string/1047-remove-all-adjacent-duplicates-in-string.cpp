class Solution {
public:
    string removeDuplicates(string s) {
        vector<char> st;
        for (char c : s) {
            if (!st.empty() && st.back() == c) {
                st.pop_back();
            }
            else {
                st.push_back(c);
            }
        }
        return string(st.begin(), st.end());
    }
};