class BrowserHistory {
public:
    vector<string> st;
    int cur = 0, ma = 0;
    BrowserHistory(string homepage) {
        st.push_back(homepage);
    }
    
    void visit(string url) {
        cur++;
        ma = cur;
        if (cur == st.size()) {
            st.push_back(url);
        }
        else {
            st[cur] = url;
        }
    }
    
    string back(int steps) {
        cur = max(cur-steps, 0);
        return st[cur];
    }
    
    string forward(int steps) {
        cur = min(cur+steps, ma);
        return st[cur];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */