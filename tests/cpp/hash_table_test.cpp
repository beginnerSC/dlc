#include <gtest/gtest.h>
#include "dlc_core/hash_table.h"

TEST(HashTableTest, TwoSum) {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    EXPECT_EQ(twoSum(nums, target), std::make_pair(0, 1));
}