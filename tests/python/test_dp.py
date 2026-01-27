"""Unit tests for dynamic programming functions."""
from dlc.dp import wordBreak, canJump


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
