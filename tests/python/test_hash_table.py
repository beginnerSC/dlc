from dlc.hash_table import containsDuplicate, twoSum


class TestContainsDuplicate:
    def test_has_duplicate(self):
        assert containsDuplicate([1, 2, 3, 1]) is True

    def test_no_duplicate(self):
        assert containsDuplicate([1, 2, 3, 4]) is False

    def test_all_duplicates(self):
        assert containsDuplicate([1, 1, 1, 1]) is True

    def test_single_element(self):
        assert containsDuplicate([42]) is False

    def test_empty_list(self):
        assert containsDuplicate([]) is False

    def test_two_same_elements(self):
        assert containsDuplicate([5, 5]) is True

    def test_negative_numbers(self):
        assert containsDuplicate([-1, -2, -3, -1]) is True

    def test_large_range_no_duplicate(self):
        nums = list(range(1000))
        assert containsDuplicate(nums) is False

    def test_large_range_with_duplicate(self):
        nums = list(range(1000)) + [999]
        assert containsDuplicate(nums) is True


class TestTwoSum:
    def test_basic_case(self):
        """Test basic word break case."""
        nums = [2, 7, 11, 15]
        target = 9

        assert twoSum(nums, target) == [0, 1]