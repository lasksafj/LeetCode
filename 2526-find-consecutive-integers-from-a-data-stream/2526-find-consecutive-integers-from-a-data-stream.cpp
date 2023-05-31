class DataStream {
public:
    int v;
    int k;
    int cnt = 0;
    int f = 0;
    DataStream(int value, int _k) {
        v = value;
        k = _k;
        f = _k;
    }
    
    bool consec(int num) {
        cnt++;
        if (num == v) {
            f--;
            if (f <= 0 and cnt >= k)
                return true;
            
            return false;
        }
        f = k;
        return false;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */