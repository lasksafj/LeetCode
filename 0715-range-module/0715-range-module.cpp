#define N 1000000000

struct node {
    node *left = NULL, *right = NULL;
    int val = 0, 
        lazy = -1, 
        l ,r;
    
    node(int _l, int _r) {
        l = _l;
        r = _r;
    }
};

class RangeModule {
public:
    node* root = new node(1,N);
    
    RangeModule() {
        
    }
    
    void push(node* cur) {
        int l = cur->l,
            r = cur->r;
        int mi = (l+r)/2,
            lazy = cur->lazy;
        if (!cur->left) 
            cur->left = new node(l, mi);
        if (!cur->right) 
            cur->right = new node(mi+1, r);
        
        if (lazy > -1) {
            cur->left->val = lazy;
            cur->left->lazy = lazy;
            cur->right->val = lazy;
            cur->right->lazy = lazy;
            cur->lazy = -1;
        }
    }
    
    void update(node* cur, int ql, int qr, bool val) {
        int l = cur->l,
            r = cur->r;
        if (l == ql && r == qr) {
            cur->val = val;
            cur->lazy = val;
        }
        else {
            push(cur);
            int mi = (l+r)/2;
            if (qr <= mi)
                update(cur->left, ql, qr, val);
            else if (mi+1 <= ql)
                update(cur->right, ql, qr, val);
            else {
                update(cur->left, ql, mi, val);
                update(cur->right, mi+1, qr, val);
            }
            cur->val = min(cur->left->val, cur->right->val);
        }
    }
    
    int query(node* cur, int ql, int qr) {
        int l = cur->l,
            r = cur->r;
        if (l == ql && r == qr) {
            return cur->val;
        }
        push(cur);
        int mi = (l+r)/2;
        if (qr <= mi)
            return query(cur->left, ql, qr);
        if (mi+1 <= ql)
            return query(cur->right, ql, qr);
        return min( query(cur->left, ql, mi), query(cur->right, mi+1, qr) );
    }
    
    void addRange(int left, int right) {
        update(root, left, right-1, 1);
    }
    
    bool queryRange(int left, int right) {
        return query(root, left, right-1);
    }
    
    void removeRange(int left, int right) {
        update(root, left, right-1, 0);
    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */