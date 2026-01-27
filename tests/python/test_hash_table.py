from dlc.hash_table import twoSum


class TestTwoSum:
    def test_basic_case(self):
        """Test basic word break case."""
        nums = [2, 7, 11, 15]
        target = 9

        assert twoSum(nums, target) == [0, 1]