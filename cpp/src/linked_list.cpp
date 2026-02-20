#include "dlc_core/linked_list.h"

ListNode* reverseList(ListNode* head) {     // 206. Reverse Linked List
    ListNode* cur = nullptr;
    while (head) {
        cur = new ListNode(head->val, cur);
        head = head->next;
    }
    return cur;
}

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {     // 21. Merge Two Sorted Lists
    ListNode* cur = new ListNode();
    ListNode* res = cur;

    while (list1 && list2) {
        if (list1->val < list2->val) {
            cur->next = new ListNode(list1->val);
            list1 = list1->next;
            cur = cur->next;
        } else {
            cur->next = new ListNode(list2->val);
            list2 = list2->next;
            cur = cur->next;
        }
    }
    cur->next = list1 ? list1 : list2;
    return res->next;
}