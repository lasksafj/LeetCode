class RandomizedSet {
public:
    unordered_map<int,int> m;
    vector<int> v;
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (m.find(val) == m.end() || m[val] == -1) {
            v.push_back(val);
            m[val] = v.size() - 1;
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if (m.find(val) != m.end() && m[val] > -1) {
            m[v.back()] = m[val];
            swap(v[m[val]], v.back());
            v.pop_back();
            m[val] = -1;
            return true;
        }
        return false;
    }
    
    int getRandom() {
        return v[rand() % v.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */