class DataStream {
public:
    int v;
    int k;
    int cnt = 0;
    queue<int> q;
    DataStream(int value, int _k) {
        v = value;
        k = _k;
    }
    
    bool consec(int num) {
        if (q.size() == k) {
            if (q.front() == v)
                cnt--;
            q.pop();
        }
        q.push(num);
        if (num == v)
            cnt++;
        return cnt == k;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */