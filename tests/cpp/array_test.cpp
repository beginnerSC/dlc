#include <gtest/gtest.h>
#include "dlc_core/array.h"

TEST(ArrayTest, LengthOfLongestSubstring) {
    EXPECT_EQ(lengthOfLongestSubstring("abcabcbb"), 3);
    EXPECT_EQ(lengthOfLongestSubstring("bbbbb"), 1);
    EXPECT_EQ(lengthOfLongestSubstring("pwwkew"), 3);
}

TEST(ArrayTest, ProductExceptSelf) {
    std::vector<int> nums = {1, 2, 3, 4};
    std::vector<int> res = {24, 12, 8, 6};
    EXPECT_EQ(productExceptSelf(nums), res);
}