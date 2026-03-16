"""Unit tests for math functions."""
from dlc.math import maximumProduct


class TestMaximumProduct:
    def test_all_positive(self):
        """Three largest positives give the max product."""
        assert maximumProduct([1, 2, 3, 4]) == 24

    def test_all_negative(self):
        """With all negatives the three least-negative (closest to 0) win."""
        assert maximumProduct([-4, -3, -2, -1]) == -6

    def test_mixed_two_negatives_dominate(self):
        """Two large negatives * largest positive can beat three largest."""
        assert maximumProduct([-10, -10, 1, 3, 2]) == 300

    def test_mixed_three_positives_dominate(self):
        """Three large positives beat any negative pair combination."""
        assert maximumProduct([-1, -2, 5, 6, 7]) == 210

    def test_minimum_three_elements(self):
        """Exactly three elements — only one product is possible."""
        assert maximumProduct([1, 2, 3]) == 6

    def test_minimum_three_all_negative(self):
        """Three negative elements."""
        assert maximumProduct([-3, -2, -1]) == -6

    def test_contains_zero(self):
        """Zero in array; two negatives * positive still wins."""
        assert maximumProduct([-5, -4, 0, 3]) == 60

    def test_contains_zeros_dominates(self):
        """Zeros among positives; product of top three is still best."""
        assert maximumProduct([0, 0, 2, 3]) == 0

    def test_large_values(self):
        """Large integers."""
        assert maximumProduct([1000, 999, 998, 1]) == 1000 * 999 * 998

    def test_repeated_values(self):
        """Repeated maximum values."""
        assert maximumProduct([3, 3, 3, 1]) == 27

    def test_single_negative_rest_positive(self):
        """One negative; three positives give the answer."""
        assert maximumProduct([-1, 2, 3, 4]) == 24
