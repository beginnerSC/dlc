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

TEST(LinkedListTest, MergeTwoLists_BothNonEmpty) {
    // Create list1: 1 -> 2 -> 4
    ListNode* list1 = new ListNode(1);
    list1->next = new ListNode(2);
    list1->next->next = new ListNode(4);
    
    // Create list2: 1 -> 3 -> 4
    ListNode* list2 = new ListNode(1);
    list2->next = new ListNode(3);
    list2->next->next = new ListNode(4);
    
    // Merge the lists
    ListNode* merged = mergeTwoLists(list1, list2);
    
    // Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    EXPECT_EQ(merged->val, 1);
    EXPECT_EQ(merged->next->val, 1);
    EXPECT_EQ(merged->next->next->val, 2);
    EXPECT_EQ(merged->next->next->next->val, 3);
    EXPECT_EQ(merged->next->next->next->next->val, 4);
    EXPECT_EQ(merged->next->next->next->next->next->val, 4);
    EXPECT_EQ(merged->next->next->next->next->next->next, nullptr);
}

TEST(LinkedListTest, MergeTwoLists_BothEmpty) {
    // Create two empty lists
    ListNode* list1 = nullptr;
    ListNode* list2 = nullptr;
    
    // Merge the lists
    ListNode* merged = mergeTwoLists(list1, list2);
    
    // Expected: nullptr (empty list)
    EXPECT_EQ(merged, nullptr);
}

TEST(LinkedListTest, MergeTwoLists_OneEmpty) {
    // Create empty list1
    ListNode* list1 = nullptr;
    
    // Create list2: 0
    ListNode* list2 = new ListNode(0);
    
    // Merge the lists
    ListNode* merged = mergeTwoLists(list1, list2);
    
    // Expected: 0
    EXPECT_EQ(merged->val, 0);
    EXPECT_EQ(merged->next, nullptr);
}