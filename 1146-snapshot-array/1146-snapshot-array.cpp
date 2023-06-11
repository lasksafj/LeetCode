class SnapshotArray {
public:
    vector<map<int,int>> a;
    int sn = 0;
    SnapshotArray(int length) {
        a = vector<map<int,int>>(length);
        for (auto& e:a) {
            e[0] = 0;
        }
    }
    
    void set(int index, int val) {
        a[index][sn] = val;
    }
    
    int snap() {
        sn++;
        return sn-1;
    }
    
    int get(int index, int snap_id) {
        auto it = a[index].upper_bound(snap_id);
        if (it == a[index].begin())
            return it->second;
        return (--it)->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */