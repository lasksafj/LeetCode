class RandomizedCollection {
public:
    unordered_map<int,vector<int>> m;
    vector<pair<int,int>> v;
    RandomizedCollection() {
        
    }
    
    bool insert(int val) {
        bool res = m.find(val) == m.end() || m[val].size() == 0;
        m[val].push_back(v.size());
        v.push_back({val, m[val].size()-1});
        return res;
    }
    
    bool remove(int val) {
        if (m[val].size() > 0) {
            int p = m[val].back();
            m[v.back().first][v.back().second] = p;
            swap(v[p], v.back());
            v.pop_back();
            m[val].pop_back();
            return true;
        }
        return false;
    }
    
    int getRandom() {
        return v[rand() % v.size()].first;
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */