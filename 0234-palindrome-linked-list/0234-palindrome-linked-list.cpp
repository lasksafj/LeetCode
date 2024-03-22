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
    bool isPalindrome(ListNode* head) {
        ListNode dum(0, head);
        ListNode* a = head, *b = head,
                *prev = &dum, *cur = head, *tmp;
        while (b && b->next) {
            a = a->next;
            b = b->next->next;
            
            tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
            
        }
        if (b)
            a = a->next;
        tmp = b = prev;
        prev = cur;
        cur = tmp;
        // cout<<a->val<<" "<<b->val;
        bool res = 1;
        while (a) {
            if (a->val != b->val) {
                res = 0;
            }
            a = a->next;
            b = b->next;
            
            tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }
        return res;
    }
};