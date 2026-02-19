"""Unit tests for dynamic programming functions."""
from dlc.dp import wordBreak, canJump, findLength, longestCommonSubsequence, uniquePaths

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
