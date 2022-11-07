class RandomizedCollection {
public:
    unordered_map<int,unordered_set<int>> m;
    vector<int> v;
    RandomizedCollection() {
        
    }
    
    bool insert(int val) {
        bool res = m.find(val) == m.end() || m[val].size() == 0;
        m[val].insert(v.size());
        v.push_back(val);
        return res;
    }
    
    bool remove(int val) {
        if (m[val].size() > 0) {
            int p = *m[val].begin();
            m[val].erase(p);
            v[p] = v.back();
            m[v[p]].insert(p);
            m[v[p]].erase(v.size()-1);
            v.pop_back();
            return true;
        }
        return false;
    }
    
    int getRandom() {
        return v[rand() % v.size()];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */