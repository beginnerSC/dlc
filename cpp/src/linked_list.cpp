#include "dlc_core/linked_list.h"

ListNode* reverseList(ListNode* head) {     // 206. Reverse Linked List
    ListNode* cur = nullptr;
    while (head) {
        cur = new ListNode(head->val, cur);
        head = head->next;
    }
    return cur;
}