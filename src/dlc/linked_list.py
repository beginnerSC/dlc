from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    """141. Linked List Cycle"""
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    
    return False

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """206. Reverse Linked List"""
    cur = None
    while head:
        cur = ListNode(head.val, cur)
        head = head.next
    return cur

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """21. Merge Two Sorted Lists"""

    dummy = cur = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next
        else:
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next

    cur.next = list1 if list1 else list2
    return dummy.next
