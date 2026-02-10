#include <gtest/gtest.h>
#include "dlc_core/dp.h"

TEST(DpTest, WordBreakAB) {
    // Test basic word break case.
    std::string s = "a";
    std::vector<std::string> wordDict = {"b"};
    EXPECT_EQ(wordBreak(s, wordDict), false);
}

TEST(DpTest, WordBreakBasicCase) {
    // Test basic word break case.
    std::string s = "leetcode";
    std::vector<std::string> wordDict = {"leet", "code"};
    EXPECT_EQ(wordBreak(s, wordDict), true);
}

TEST(DpTest, WordBreakNoBreakPossible) {
    // Test when word break is not possible.
    std::string s = "catsandog";
    std::vector<std::string> wordDict = {"cats", "dog", "sand", "and", "cat"};
    EXPECT_EQ(wordBreak(s, wordDict), false);
}

TEST(DpTest, WordBreakReusableWords) {
    // Test with reusable words.
    std::string s = "applepenapple";
    std::vector<std::string> wordDict = {"apple", "pen"};
    EXPECT_EQ(wordBreak(s, wordDict), true);
}

TEST(DpTest, LongestCommonSubsequence) {
    EXPECT_EQ(longestCommonSubsequence("abcde", "ace"), 3);
    EXPECT_EQ(longestCommonSubsequence("abc", "abc"), 3);
    EXPECT_EQ(longestCommonSubsequence("abc", "def"), 0);
}

TEST(DpTest, FindLength) {
    std::vector<int> nums1 = {1, 2, 3, 2, 1}; 
    std::vector<int> nums2 = {3, 2, 1, 4, 7};
    EXPECT_EQ(findLength(nums1, nums2), 3);

    nums1 = {0, 0, 0, 0, 0}; 
    nums2 = nums1;
    EXPECT_EQ(findLength(nums1, nums2), 5);
}

TEST(DpTest, HouseRobber) {
    std::vector<int> nums1 = {1, 2, 3, 1};
    EXPECT_EQ(rob(nums1), 4);

    std::vector<int> nums2 = {2, 7, 9, 3, 1};
    EXPECT_EQ(rob(nums2), 12);

    std::vector<int> nums3 = {2, 1, 1, 2};
    EXPECT_EQ(rob(nums3), 4);
}

TEST(DpTest, CoinChange) {
    std::vector<int> coins = {1, 2, 5};
    int amount = 11;
    EXPECT_EQ(coinChange(coins, amount), 3);

    ////////// will break the code //////////
    // std::vector<int> coins = {2}; 
    // int amount = 3;
    // EXPECT_EQ(coinChange(coins, amount), -1);
}

TEST(DpTest, climbStairs) {
    EXPECT_EQ(climbStairs(5), 8);
}