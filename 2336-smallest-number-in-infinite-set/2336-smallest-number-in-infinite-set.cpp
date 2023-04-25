class SmallestInfiniteSet {
public:
    set<int> ban;
    int res;
    SmallestInfiniteSet() {
        res = 1;
    }
    
    int popSmallest() {
        while (ban.find(res) != ban.end()) {
            res++;
        }
        ban.insert(res);
        return res;
    }
    
    void addBack(int num) {
        if (ban.find(num) != ban.end()) {
            ban.erase(num);
        }
        res = min(res, num);
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */