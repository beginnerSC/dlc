"""Unit tests for array functions."""
from dlc.array import productExceptSelf, maxSubArray, lengthOfLongestSubstring, lengthOfLongestSubstring1


class TestLengthOfLongestSubstring:
    def test_basic_case(self):
        for f in [lengthOfLongestSubstring, lengthOfLongestSubstring1]:
            assert f("abcabcbb") == 3
            assert f("bbbbb") == 1
            assert f("pwwkew") == 3


class TestMaxSubArray:
    def test_basic_case(self):
        assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
        assert maxSubArray([1]) == 1
        assert maxSubArray([5,4,-1,7,8]) == 23


class TestProductExceptSelf:
    def test_basic_case(self):
        """Test basic product except self."""
        nums = [1, 2, 3, 4]
        assert productExceptSelf(nums) == [24, 12, 8, 6]
    
    def test_with_zero(self):
        """Test with zero in array."""
        nums = [1, 0, 3, 4]
        assert productExceptSelf(nums) == [0, 12, 0, 0]
    
    def test_multiple_zeros(self):
        """Test with multiple zeros."""
        nums = [0, 0, 3, 4]
        assert productExceptSelf(nums) == [0, 0, 0, 0]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, 1, 0, -3, 3]
        assert productExceptSelf(nums) == [0, 0, 9, 0, 0]
