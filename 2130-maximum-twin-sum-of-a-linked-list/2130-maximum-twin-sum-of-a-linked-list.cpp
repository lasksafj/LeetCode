/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> a;
        auto p = head;
        while(p) {
            a.push_back(head->val);
            p = p->next->next;
            head = head->next;
        }
        int res = 0;
        for (int i = a.size()-1; i >= 0; i--) {
            res = max(res, a[i] + head->val);
            head = head->next;
        }
        return res;
    }
};