class Solution {
public:
    set<int> vis;
    unordered_map<int,int> M;
    int dfs(int i, int d, vector<int>& edges) {
        vis.insert(i);
        M[i] = d;
        int res = -1;
        if (edges[i] != -1 && vis.find(edges[i]) == vis.end()) {
            res = dfs(edges[i], d+1, edges);
        }
        else {
            // cout<<i<<" "<<edges[i]<<" "<<M[i]<<" "<<M[edges[i]]<<endl;
            res = M[i] - M[edges[i]] + 1;
        }
        M[i] = 1000000;
        return res;
    }
    
    int longestCycle(vector<int>& edges) {
        int res = 0;
        M[-1] = 1000000;
        for (int i = 0; i < edges.size(); i++) {
            if (vis.find(i) == vis.end())
                res = max(res, dfs(i, 0, edges));
            M[i] = 1000000;
        }
        return res > 0? res:-1;
    }
};