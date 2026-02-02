#include <gtest/gtest.h>
#include "dlc_core/linked_list.h"


TEST(LinkedListTest, ReverseList) {
    // Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    
    // Reverse the list
    ListNode* reversed = reverseList(head);
    
    // Expected: 5 -> 4 -> 3 -> 2 -> 1
    EXPECT_EQ(reversed->val, 5);
    EXPECT_EQ(reversed->next->val, 4);
    EXPECT_EQ(reversed->next->next->val, 3);
    EXPECT_EQ(reversed->next->next->next->val, 2);
    EXPECT_EQ(reversed->next->next->next->next->val, 1);
    EXPECT_EQ(reversed->next->next->next->next->next, nullptr);
}