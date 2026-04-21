
from typing import List
import heapq

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """239. Sliding Window Maximum"""

    n = len(nums)
    nums = [-num for num in nums]
    heap = list(zip(nums[:k], range(k)))
    heapq.heapify(heap)
    res = [heap[0][0]]

    for i, j in zip(range(1, n-k+1), range(k, n)):
        heapq.heappush(heap, (nums[j], j))
        while heap[0][1] < i:
            heapq.heappop(heap)
        res.append(heap[0][0])
    
    return [-num for num in res]

class IndexedPriorityQueue:
    def __init__(self, capacity):
        """
        capacity: maximum index range (0 to capacity-1)
        """
        self.capacity = capacity
        # Think about how to initialize the following structures:
        # 1. Array storing priority values (values)
        # 2. Heap array storing indices (heap)
        # 3. Mapping from index to heap position for fast lookup (pos)
        pass

    def is_empty(self):
        """Check whether the queue is empty"""
        pass

    def contains(self, i):
        """Check whether index i is already in the queue"""
        pass

    def insert(self, i, value):
        """Insert index i with its associated priority value"""
        pass

    def peek_min_index(self):
        """Return the index with the minimum priority value without removing it"""
        pass

    def peek_min_value(self):
        """Return the minimum priority value without removing it"""
        pass

    def pop_min_index(self):
        """Pop and return the index with the minimum priority value, then re-heapify"""
        pass

    def update(self, i, new_value):
        """Update the priority value of index i, then swim or sink as appropriate"""
        pass

    def delete(self, i):
        """Remove index i from the queue entirely"""
        pass

    # --- Internal private helper methods (core logic) ---

    def _swim(self, p):
        """Bubble up from heap position p"""
        pass

    def _sink(self, p):
        """Sink down from heap position p"""
        pass

    def _swap(self, p1, p2):
        """
        Swap the elements at heap positions p1 and p2.
        Note: besides swapping values in the heap array, the pos array must be updated in sync!
        """
        pass