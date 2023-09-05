/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head)  return NULL;
        unordered_map<Node*, Node*> m;
        Node* hh = head;
        Node dummy(0);
        Node* h = &dummy;
        while (head) {
            h->next = new Node(head->val);
            h = h->next;
            m[head] = h;
            head = head->next;
        }
        h = dummy.next;
        while (hh) {
            h->random = m[hh->random];
            h = h->next;
            hh = hh->next;
        }
        return dummy.next;
    }
};