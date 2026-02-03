"""Unit tests for binary search functions."""
from dlc.bsearch import search

class TestSearch:
    def test_bsearch(self):
        assert search(nums=[-1,0,3,5,9,12], target=9) == 4
        assert search(nums=[-1,0,3,5,9,12], target=2) == -1