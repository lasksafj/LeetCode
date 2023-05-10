class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n));
        int cnt = 1;
        int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int d = 0;
        int r = 0;
        int c = 0;
        for (int i = 0; i < n*n; i++) {
            res[r][c] = cnt++;
            int nr = r+dir[d][0],
                nc = c+dir[d][1];
            if (nr >= n || nc >= n || nr < 0 || nc < 0 || res[nr][nc] != 0)
                d = (d+1)%4;
            r += dir[d][0];
            c += dir[d][1];
        }
        return res;
    }
};