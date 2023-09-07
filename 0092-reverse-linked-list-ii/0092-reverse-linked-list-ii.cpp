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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode dum(0, head);
        ListNode* h = &dum;
        int len = right - left;
        while (left-- > 1) {
            h = h->next;
        }
        ListNode *a = h, *b = h->next, *prev = h,
                 *cur = h->next,
                 *tmp;
        if (!cur)
            return h;
        while (len-- > -1) {
            tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }
        a->next = prev;
        b->next = cur;
        return dum.next;
    }
};