class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> m;
        for (string& w : strs) {
            string tmp = w;
            sort(tmp.begin(), tmp.end());
            m[tmp].push_back(w);
        }
        vector<vector<string>> res;
        for (auto& e : m) {
            res.push_back(e.second);
        }
        return res;
    }
};