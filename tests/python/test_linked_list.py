"""Unit tests for linked list functions."""
from dlc.linked_list import ListNode, reverseList, mergeTwoLists


def list_to_array(head):
    """Helper: Convert linked list to array."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    """Helper: Convert array to linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class TestReverseList:
    def test_basic_case(self):
        """Test reversing a basic list."""
        head = array_to_list([1, 2, 3, 4, 5])
        result = reverseList(head)
        assert list_to_array(result) == [5, 4, 3, 2, 1]
    
    def test_empty_list(self):
        """Test reversing an empty list."""
        assert reverseList(None) is None
    
    def test_single_element(self):
        """Test reversing a single element list."""
        head = array_to_list([1])
        result = reverseList(head)
        assert list_to_array(result) == [1]


class TestMergeTwoLists:
    def test_basic_merge(self):
        """Test merging two basic sorted lists."""
        list1 = array_to_list([1, 2, 4])
        list2 = array_to_list([1, 3, 4])
        result = mergeTwoLists(list1, list2)
        assert list_to_array(result) == [1, 1, 2, 3, 4, 4]
    
    def test_empty_lists(self):
        """Test merging two empty lists."""
        result = mergeTwoLists(None, None)
        assert result is None
    
    def test_one_empty(self):
        """Test merging when one list is empty."""
        list1 = array_to_list([1, 2, 3])
        result = mergeTwoLists(list1, None)
        assert list_to_array(result) == [1, 2, 3]
        
        list2 = array_to_list([1, 2, 3])
        result = mergeTwoLists(None, list2)
        assert list_to_array(result) == [1, 2, 3]
