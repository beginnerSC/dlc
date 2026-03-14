"""Unit tests for dynamic programming functions."""
from dlc.dp import coinChange, wordBreak, canJump, findLength, longestCommonSubsequence, uniquePaths, fib, rob, maximalSquare


class TestCoinChange:
    def test_example_case(self):
        assert coinChange([1, 2, 5], 11) == 3

    def test_unreachable_amount(self):
        assert coinChange([2], 3) == -1

    def test_zero_amount(self):
        assert coinChange([1, 2, 5], 0) == 0

    def test_single_coin_exact_match(self):
        assert coinChange([7], 14) == 2

    def test_prefers_minimum_number_of_coins(self):
        assert coinChange([1, 3, 4], 6) == 2

    def test_unsorted_coin_values(self):
        assert coinChange([5, 1, 2], 11) == 3

class TestFib:
    def test_base_case_zero(self):
        assert fib(0) == 0

    def test_base_case_one(self):
        assert fib(1) == 1

    def test_small_values(self):
        assert fib(2) == 1
        assert fib(3) == 2
        assert fib(4) == 3
        assert fib(5) == 5

    def test_larger_value(self):
        assert fib(10) == 55

    def test_known_value(self):
        assert fib(20) == 6765

class TestUniquePaths:
    def test_basic_case_1(self):
        """Test case: m = 3, n = 7, expecting 28 unique paths."""
        assert uniquePaths(3, 7) == 28
    
    def test_basic_case_2(self):
        """Test case: m = 3, n = 2, expecting 3 unique paths."""
        assert uniquePaths(3, 2) == 3
    
    def test_single_cell(self):
        """Test with a 1x1 grid."""
        assert uniquePaths(1, 1) == 1
    
    def test_small_grid(self):
        """Test with a 2x2 grid."""
        assert uniquePaths(2, 2) == 2

class TestLongestCommonSubsequence:
    def test_basic_case(self):
        assert longestCommonSubsequence("abcde", "ace") == 3
        assert longestCommonSubsequence("abc", "abc") == 3
        assert longestCommonSubsequence("abc", "def") == 0

class TestFindLength:
    def test_basic_case(self):
        nums1 = [1,2,3,2,1]
        nums2 = [3,2,1,4,7]
        assert findLength(nums1, nums2) == 3

        nums1 = [0,0,0,0,0]
        nums2 = [0,0,0,0,0]
        assert findLength(nums1, nums2) == 5

class TestWordBreak:
    def test_basic_case(self):
        """Test basic word break case."""
        s = "leetcode"
        wordDict = ["leet", "code"]
        assert wordBreak(s, wordDict) == True
    
    def test_no_break_possible(self):
        """Test when word break is not possible."""
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        assert wordBreak(s, wordDict) == False
    
    def test_reusable_words(self):
        """Test with reusable words."""
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        assert wordBreak(s, wordDict) == True

class TestCanJump:
    def test_can_reach_end(self):
        """Test when we can reach the end."""
        assert canJump([2, 3, 1, 1, 4]) == True
    
    def test_cannot_reach_end(self):
        """Test when we cannot reach the end."""
        assert canJump([3, 2, 1, 0, 4]) == False
    
    def test_single_element(self):
        """Test with single element array."""
        assert canJump([0]) == True
    
    def test_zero_at_start(self):
        """Test with zero at start."""
        assert canJump([0, 1]) == False


class TestRob:
    def test_basic_case(self):
        """Canonical House Robber example."""
        assert rob([1, 2, 3, 1]) == 4

    def test_second_basic_case(self):
        """Another common House Robber example."""
        assert rob([2, 7, 9, 3, 1]) == 12

    def test_single_house(self):
        """Single house should return its own value."""
        assert rob([5]) == 5

    def test_two_houses(self):
        """Choose the maximum of two houses."""
        assert rob([2, 1]) == 2

    def test_non_adjacent_best(self):
        """Best answer may skip multiple local maxima."""
        assert rob([2, 1, 1, 2]) == 4


class TestMaximalSquare:
    def test_example_case(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        assert maximalSquare(matrix) == 4

    def test_small_mixed_case(self):
        matrix = [["0", "1"], ["1", "0"]]
        assert maximalSquare(matrix) == 1

    def test_single_zero(self):
        assert maximalSquare([["0"]]) == 0

    def test_single_one(self):
        assert maximalSquare([["1"]]) == 1

    def test_all_ones_square(self):
        matrix = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"],
        ]
        assert maximalSquare(matrix) == 9
