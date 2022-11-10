class Solution {
public:
    vector<string> twoEditWords(vector<string>& q, vector<string>& d) {
        vector<string>ans;
        for(int i=0;i<q.size();i++){
           for(int j=0;j<d.size();j++){
               if(getDiff(q[i],d[j])){
                   ans.push_back(q[i]);
                   break;
               }
           }
        }
        return ans;
        
    }
    
    bool getDiff(string &s1,string &s2){
        int diff=0;
        for(int i=0;i<s1.size();i++){
            if(s1[i]!=s2[i]){
                diff++;
            }
            if(diff>2){
                return false;
            }
        }
        return true;
    }
    
};