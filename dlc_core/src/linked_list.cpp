#include "dlc_core/linked_list.h"

ListNode* reverseList(ListNode* head) {
    ListNode* cur = nullptr;
    while (head) {
        cur = new ListNode(head->val, cur);
        head = head->next;
    }
    return cur;
}