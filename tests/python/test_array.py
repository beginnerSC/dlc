"""Unit tests for array functions."""
from dlc.array import (
    productExceptSelf,
    maxSubArray,
    lengthOfLongestSubstring,
    lengthOfLongestSubstring1,
    maxProfit,
)


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


class TestMaxProfit:
    def test_examples(self):
        """LeetCode 121 canonical examples."""
        assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
        assert maxProfit([7, 6, 4, 3, 1]) == 0

    def test_minimal_sizes(self):
        """Single day and two days."""
        assert maxProfit([5]) == 0
        assert maxProfit([1, 2]) == 1
        assert maxProfit([2, 1]) == 0

    def test_flat_and_repeated_prices(self):
        """No gain when prices never rise."""
        assert maxProfit([3, 3, 3, 3]) == 0
        assert maxProfit([2, 2, 1, 1]) == 0

    def test_best_buy_not_first_day(self):
        """Best buy can occur after an early peak."""
        assert maxProfit([5, 4, 3, 2, 10]) == 8

    def test_best_sell_not_last_day(self):
        """Best sell may happen before the final day."""
        assert maxProfit([1, 9, 2, 3]) == 8
