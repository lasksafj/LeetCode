class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> r[9], c[9], b[9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char cur = board[i][j];
                if (cur == '.')
                    continue;
                if (r[i].find(cur) != r[i].end() 
                    || c[j].find(cur) != c[j].end()
                    || b[i/3*3 + j/3].find(cur) != b[i/3*3 + j/3].end())
                    return false;
                r[i].insert(cur), c[j].insert(cur), b[i/3*3 + j/3].insert(cur);
            }
        }
        return true;
    }
};