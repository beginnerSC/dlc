#include <gtest/gtest.h>
#include "dlc_core/array.h"

TEST(ArrayTest, MaxSubArray) {
    std::vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    int res = 6;
    EXPECT_EQ(maxSubArray(nums), res);

    nums = {1};
    res = 1;
    EXPECT_EQ(maxSubArray(nums), res);

    nums = {5,4,-1,7,8};
    res = 23;
    EXPECT_EQ(maxSubArray(nums), res);

    nums = {-1};
    res = -1;
    EXPECT_EQ(maxSubArray(nums), res);
}

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