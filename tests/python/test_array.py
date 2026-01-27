"""Unit tests for array functions."""
from dlc.array import productExceptSelf


class TestProductExceptSelf:
    def test_basic_case(self):
        """Test basic product except self."""
        nums = [1, 2, 3, 4]
        result = productExceptSelf(nums)
        expected = [24, 12, 8, 6]
        assert result == expected
    
    def test_with_zero(self):
        """Test with zero in array."""
        nums = [1, 0, 3, 4]
        result = productExceptSelf(nums)
        expected = [0, 12, 0, 0]
        assert result == expected
    
    def test_multiple_zeros(self):
        """Test with multiple zeros."""
        nums = [0, 0, 3, 4]
        result = productExceptSelf(nums)
        expected = [0, 0, 0, 0]
        assert result == expected
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, 1, 0, -3, 3]
        result = productExceptSelf(nums)
        expected = [0, 0, 9, 0, 0]
        assert result == expected
