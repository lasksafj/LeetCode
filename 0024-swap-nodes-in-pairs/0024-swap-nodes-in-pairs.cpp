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
    ListNode* swapPairs(ListNode* head) {
        if (!head)
            return NULL;
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        while (head && head->next) {
            prev->next = head->next;
            head->next = head->next->next;
            prev->next->next = head;
            prev = head;
            head = head->next;
        }
        return dummy.next;
    }
};