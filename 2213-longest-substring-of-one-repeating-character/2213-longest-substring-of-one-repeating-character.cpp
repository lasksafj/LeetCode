class Solution {
public:
    struct node {
        char lc = 0, rc = 0;
        int pre = 1, suf = 1, longest = 1, sz = 1;
        void merge(node& l, node& r) {
            longest = max(l.longest, r.longest);
            if (l.rc == r.lc) {
                longest = max(longest, l.suf + r.pre);
            }
            lc = l.lc;
            rc = r.rc;
            sz = l.sz + r.sz;
            pre = l.pre + (l.rc == r.lc && l.pre == l.sz? r.pre : 0);
            suf = r.suf + (l.rc == r.lc && r.suf == r.sz? l.suf : 0);
        }
    };
    
    void update(vector<node>& T, int i, int l, int r, int p, char ch) {
        if (l <= p && p < r) {
            if (l == r-1) {
                T[i].lc = T[i].rc = ch;
            }
            else {
                int mi = (l+r)/2;
                update(T, i*2+1, l, mi, p, ch);
                update(T, i*2+2, mi, r, p, ch);
                T[i].merge(T[i*2+1], T[i*2+2]);
            }
        }
    }
    
    int query(vector<node>& T, int i, int l, int r, int ql, int qr) {
        int res = 0;
        if (l <= ql && qr <= r) {
            res = T[i].longest;
        }
        else if (r <= ql || qr <= l) {
            return 0;
        }
        else {
            int mi = (l+r)/2;
            res = max(query(T, i*2+1, l, mi, ql, qr), query(T, i*2+2, mi, r, ql, qr));
        }
        return res;
    }
    
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        vector<int> res;
        int powOf2 = 1, sz = s.size();
        while (powOf2 < sz) 
            powOf2 <<= 1;
        vector<node> T(powOf2*2);
        for (int i = 0; i < sz; i++) {
            update(T, 0, 0, sz, i, s[i]);
        }
        for (int i = 0; i < queryCharacters.size(); i++) {
            update(T, 0, 0, sz, queryIndices[i], queryCharacters[i]);
            res.push_back(query(T, 0, 0, sz, 0, sz));
        }
        return res;
    }
};