class TimeMap {
public:
    unordered_map<string, map<int,string>> m;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        m[key][timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        if (m.find(key) == m.end())
            return "";
        auto& a = m[key];
        auto it = a.lower_bound(timestamp);
        if (it == a.end())
            return a.rbegin()->second;
        if (it->first == timestamp)
            return it->second;
        if (it == a.begin())
            return "";
        return (--it)->second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */