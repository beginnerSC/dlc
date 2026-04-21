import pytest
from dlc.heap import IndexedPriorityQueue, maxSlidingWindow


# class TestIndexedPriorityQueueInit:
#     def test_initial_state_is_empty(self):
#         ipq = IndexedPriorityQueue(10)
#         assert ipq.is_empty() is True

#     def test_capacity_stored(self):
#         ipq = IndexedPriorityQueue(5)
#         assert ipq.capacity == 5


# class TestIsEmpty:
#     def test_empty_on_creation(self):
#         ipq = IndexedPriorityQueue(10)
#         assert ipq.is_empty() is True

#     def test_not_empty_after_insert(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 42)
#         assert ipq.is_empty() is False

#     def test_empty_after_all_elements_popped(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 1)
#         ipq.pop_min_index()
#         assert ipq.is_empty() is True


# class TestContains:
#     def test_does_not_contain_before_insert(self):
#         ipq = IndexedPriorityQueue(10)
#         assert ipq.contains(3) is False

#     def test_contains_after_insert(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(3, 99)
#         assert ipq.contains(3) is True

#     def test_does_not_contain_after_delete(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(3, 99)
#         ipq.delete(3)
#         assert ipq.contains(3) is False

#     def test_does_not_contain_after_pop(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(2, 5)
#         ipq.pop_min_index()
#         assert ipq.contains(2) is False


# class TestInsert:
#     def test_single_insert(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(1, 10)
#         assert ipq.contains(1) is True

#     def test_multiple_inserts(self):
#         ipq = IndexedPriorityQueue(10)
#         for i, v in enumerate([30, 10, 50, 20]):
#             ipq.insert(i, v)
#         for i in range(4):
#             assert ipq.contains(i) is True

#     def test_insert_maintains_min_at_top(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 50)
#         ipq.insert(1, 10)
#         ipq.insert(2, 30)
#         assert ipq.peek_min_value() == 10


# class TestPeekMinIndex:
#     def test_single_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(4, 7)
#         assert ipq.peek_min_index() == 4

#     def test_returns_index_of_minimum(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 100)
#         ipq.insert(1, 5)
#         ipq.insert(2, 50)
#         assert ipq.peek_min_index() == 1

#     def test_does_not_remove_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(2, 3)
#         ipq.peek_min_index()
#         assert ipq.contains(2) is True


# class TestPeekMinValue:
#     def test_single_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 42)
#         assert ipq.peek_min_value() == 42

#     def test_returns_minimum_value(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 30)
#         ipq.insert(1, 10)
#         ipq.insert(2, 20)
#         assert ipq.peek_min_value() == 10

#     def test_does_not_remove_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 7)
#         ipq.peek_min_value()
#         assert ipq.is_empty() is False


# class TestPopMinIndex:
#     def test_pop_single_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(3, 99)
#         assert ipq.pop_min_index() == 3
#         assert ipq.is_empty() is True

#     def test_pop_returns_min_index(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 30)
#         ipq.insert(1, 10)
#         ipq.insert(2, 20)
#         assert ipq.pop_min_index() == 1

#     def test_pop_removes_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(1, 10)
#         ipq.pop_min_index()
#         assert ipq.contains(1) is False

#     def test_pop_maintains_heap_order(self):
#         ipq = IndexedPriorityQueue(10)
#         values = [(0, 40), (1, 10), (2, 30), (3, 20), (4, 50)]
#         for i, v in values:
#             ipq.insert(i, v)
#         popped_values = []
#         for _ in range(len(values)):
#             idx = ipq.pop_min_index()
#             popped_values.append(dict(values)[idx])
#         assert popped_values == sorted(popped_values)
#         assert ipq.is_empty() is True

#     def test_pop_all_elements_one_by_one(self):
#         ipq = IndexedPriorityQueue(5)
#         ipq.insert(0, 5)
#         ipq.insert(1, 3)
#         ipq.insert(2, 4)
#         ipq.insert(3, 1)
#         ipq.insert(4, 2)
#         expected_order = [3, 4, 1, 2, 0]  # indices sorted by their values 1,2,3,4,5
#         result = []
#         for _ in range(5):
#             result.append(ipq.pop_min_index())
#         assert result == expected_order
#         assert ipq.is_empty() is True


# class TestUpdate:
#     def test_update_to_smaller_triggers_swim(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 10)
#         ipq.insert(1, 20)
#         ipq.insert(2, 30)
#         ipq.update(2, 1)  # index 2 should now be the minimum
#         assert ipq.peek_min_index() == 2
#         assert ipq.peek_min_value() == 1

#     def test_update_to_larger_triggers_sink(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 1)
#         ipq.insert(1, 20)
#         ipq.insert(2, 30)
#         ipq.update(0, 50)  # index 0 should no longer be the minimum
#         assert ipq.peek_min_index() == 1
#         assert ipq.peek_min_value() == 20

#     def test_update_same_value(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 10)
#         ipq.update(0, 10)
#         assert ipq.peek_min_value() == 10

#     def test_update_preserves_heap_order(self):
#         ipq = IndexedPriorityQueue(10)
#         for i, v in enumerate([5, 3, 8, 1, 7]):
#             ipq.insert(i, v)
#         ipq.update(0, 0)  # make index 0 the new minimum
#         assert ipq.pop_min_index() == 0


# class TestDelete:
#     def test_delete_only_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(5, 42)
#         ipq.delete(5)
#         assert ipq.is_empty() is True
#         assert ipq.contains(5) is False

#     def test_delete_min_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 1)
#         ipq.insert(1, 5)
#         ipq.insert(2, 3)
#         ipq.delete(0)
#         assert ipq.contains(0) is False
#         assert ipq.peek_min_value() == 3

#     def test_delete_non_min_element(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 10)
#         ipq.insert(1, 5)
#         ipq.insert(2, 20)
#         ipq.delete(2)
#         assert ipq.contains(2) is False
#         assert ipq.peek_min_index() == 1

#     def test_delete_middle_element_preserves_order(self):
#         ipq = IndexedPriorityQueue(10)
#         for i, v in enumerate([4, 2, 6, 1, 8]):
#             ipq.insert(i, v)
#         ipq.delete(2)  # remove index 2 (value 6)
#         result = []
#         for _ in range(4):
#             result.append(ipq.pop_min_index())
#         assert result == [3, 1, 0, 4]  # indices sorted by values 1,2,4,8
#         assert ipq.is_empty() is True


# class TestSwap:
#     def test_swap_updates_heap_and_pos(self):
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 10)
#         ipq.insert(1, 5)
#         # After insert, index 1 (value 5) should be at top; swap should keep pos consistent
#         ipq._swap(0, 1)  # swap the top two heap positions
#         # The structure should still be query-able
#         assert not ipq.is_empty()


# class TestSwimSink:
#     def test_swim_called_on_insert(self):
#         """insert with a very small value must swim all the way to the top"""
#         ipq = IndexedPriorityQueue(10)
#         ipq.insert(0, 100)
#         ipq.insert(1, 90)
#         ipq.insert(2, 80)
#         ipq.insert(3, 1)  # smallest — must swim to top
#         assert ipq.peek_min_index() == 3

#     def test_sink_called_on_pop(self):
#         """After a pop the replacement element must sink to its correct position"""
#         ipq = IndexedPriorityQueue(10)
#         for i, v in enumerate([5, 3, 8, 1, 6]):
#             ipq.insert(i, v)
#         ipq.pop_min_index()  # removes index 3 (value 1); triggers sink
#         assert ipq.peek_min_value() == 3


class TestMaxSlidingWindow:
    def test_max_sliding_window_debug_case(self):
        """
        Debug case: nums = [9,10,9,-7,-4,-8,2,-6], k = 5
        """
        nums = [9, 10, 9, -7, -4, -8, 2, -6]
        k = 5
        expected = [10, 10, 9, 2]
        result = maxSlidingWindow(nums, k)
        
        print(f"\nInput: nums = {nums}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        
        assert result == expected, f"Expected {expected}, but got {result}"
    
    def test_max_sliding_window_simple(self):
        """Simple test case: all positive numbers"""
        nums = [1, 3, 1, 2, 0, 5]
        k = 3
        expected = [3, 3, 2, 5]
        result = maxSlidingWindow(nums, k)
        assert result == expected
    
    def test_max_sliding_window_single_window(self):
        """Window size equals array length"""
        nums = [5, 2, 8, 1]
        k = 4
        expected = [8]
        result = maxSlidingWindow(nums, k)
        assert result == expected
    
    def test_max_sliding_window_k_equals_1(self):
        """Window size of 1 should return all elements"""
        nums = [1, 3, 1, 2, 0, 5]
        k = 1
        expected = [1, 3, 1, 2, 0, 5]
        result = maxSlidingWindow(nums, k)
        assert result == expected
