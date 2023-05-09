class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(),
            n = matrix[0].size();
        vector<int> res(m*n);
        int a = 0, b = 0,
            upM = m, upN = n,
            downM = 1, downN = 0;
        int dir = 1;
        for (int i = 0; i < m*n; i++) {
            res[i] = matrix[a][b];
            if (dir == 1) {
                b++;
                if (b == upN) {
                    a++;
                    b = upN-1;
                    dir = 2;
                    upN--;
                }
            }
            else if (dir == 2) {
                a++;
                if (a == upM) {
                    a = upM-1;
                    b--;
                    dir = 3;
                    upM--;
                }
            }
            else if (dir == 3) {
                b--;
                if (b == downN-1) {
                    a--;
                    b = downN;
                    dir = 4;
                    downN++;
                }
            }
            else if (dir == 4) {
                a--;
                if (a == downM-1) {
                    a = downM;
                    b++;
                    dir = 1;
                    downM++;
                }
            }
        }
        return res;
    }
};