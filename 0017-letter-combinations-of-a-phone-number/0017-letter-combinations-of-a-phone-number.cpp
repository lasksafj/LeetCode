class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<int,vector<char>> m;
        m[2] = {'a','b','c'};
        m[3] = {'d','e','f'};
        m[5] = {'j','k','l'};
        m[4] = {'g','h','i'};
        m[6] = {'m','n','o'};
        m[7] = {'p','q','r','s'};
        m[8] = {'t','u','v'};
        m[9] = {'w','x','y','z'};
        vector<string> res;
        string path;
        sol(m, digits, 0, path, res);
        return res;
    }
    
    void sol(unordered_map<int,vector<char>>& m, string& digits, int cur, string& path, vector<string>& res) {
        if (cur == digits.size() && !path.empty()) {
            res.push_back(path);
            return;
        }
        for (char c : m[digits[cur]-'0']) {
            path.push_back(c);
            sol(m, digits, cur+1, path, res);
            path.pop_back();
        }
    }
};