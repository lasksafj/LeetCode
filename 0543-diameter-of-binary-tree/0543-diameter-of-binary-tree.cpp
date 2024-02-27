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
    int res=0;
    int diameterOfBinaryTree(TreeNode* root) {
        sol(root);
        return res-1;
    }
    
    int sol(TreeNode* r) {
        if (!r)
            return 0;
        int lp = sol(r->left);
        int rp = sol(r->right);
        res = max(res, 1+lp+rp); 
        return 1 + max(lp,rp);
    }
};