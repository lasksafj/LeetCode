class LRUCache {
public:
    int size;
    list<pair<int,int>> l;
    unordered_map<int,list<pair<int,int>>::iterator> m;
    LRUCache(int capacity) {
        size = capacity;
    }
    
    int get(int key) {    
        if (m.find(key) != m.end()) {
            l.splice(l.begin(), l, m[key]);
            return m[key]->second;
        }
        return -1;
    }
    
    void put(int key, int value) {     
        if (get(key) != -1) {
            l.begin()->second = value;
        }
        else {
            if (l.size() == size) {
                m.erase(l.back().first);
                l.pop_back();
            }
            l.push_front({key,value});
            m[key] = l.begin();
            
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */