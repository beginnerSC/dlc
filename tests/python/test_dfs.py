"""Unit tests for binary search functions."""
from dlc.dfs import numIslands

class TestSearch:
    def test_bsearch(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        assert numIslands(grid) == 3