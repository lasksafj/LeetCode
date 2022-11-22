/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> A;
    vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {
        inorder(root);
        vector<vector<int>> res;
        for (int q : queries) {
            auto it = lower_bound(A.begin(), A.end(), q);
            if (it != A.end() && *it == q)
                res.push_back({q,q});
            else if (it == A.begin())
                res.push_back({-1, *it});
            else if (it == A.end())
                res.push_back({*(it-1), -1});
            else
                res.push_back({*(it-1), *it});
        }
        return res;
    }
    
    void inorder(TreeNode* r) {
        if (!r)
            return;
        inorder(r->left);
        A.push_back(r->val);
        inorder(r->right);
    }
};