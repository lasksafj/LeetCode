class Solution {
public:
    unordered_set<int> vertical_set, diag_left_set, diag_right_set;
    void sol(int i, int n, vector<vector<string>>& res, vector<string>& path) {
        if (i == n) {
            res.push_back(path);
            return;
        }
        for (int j = 0; j < n; j++) {
            if (vertical_set.find(j) == vertical_set.end()
               && diag_left_set.find(j+i) == diag_left_set.end()
               && diag_right_set.find(j-i) == diag_right_set.end()) {
                
                vertical_set.insert(j);
                diag_left_set.insert(j+i);
                diag_right_set.insert(j-i);
                
                string cur = string(j, '.') + "Q" + string(n-j-1, '.');
                path.push_back(cur);
                // cout<<i<<"---"<<j<<" "<<j+i<<" "<<j-i<<" "<<cur<< endl;
                
                sol(i+1, n, res, path);
                
                vertical_set.erase(j);
                diag_left_set.erase(j+i);
                diag_right_set.erase(j-i);
                path.pop_back();
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> path;
        sol(0, n, res, path);
        return res;
    }
};