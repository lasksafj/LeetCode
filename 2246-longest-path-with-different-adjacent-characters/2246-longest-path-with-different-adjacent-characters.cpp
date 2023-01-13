class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        int n=s.size();
        vector<int> indegree(n,0);
        for(int i=0;i<n;i++){
            if(parent[i]!=-1){
                indegree[parent[i]]++;
            }
        }
        queue<int> q;
        for(int i=0;i<n;i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        vector<int> maxpath(n,1);
        int ans=1;
        while(!q.empty()){
            int u=q.front();
            q.pop();
            
            int v=parent[u];
            if(v==-1){
                continue;
            }
            indegree[v]--;
            if(s[u]!=s[v]){
                ans=max(ans,maxpath[v]+maxpath[u]);
                maxpath[v]=max(maxpath[v],1+maxpath[u]);
            }
            if(indegree[v]==0){
                q.push(v);
            }
        }
        return ans;
    }
};