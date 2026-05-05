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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        ListNode* cur = head;
        int len = 0;
        while (cur->next) {
            len++;
            cur = cur->next;
        }
        len++;
    
        int headPos = (len + (len-k) % len) % len;

        if (headPos > 0) {
            cur->next = head;
            cur = head;
            while(headPos-- > 1) {
                cur = cur->next;
            }
            head = cur->next;
            cur->next = NULL;
        }

        return head;
    }
};