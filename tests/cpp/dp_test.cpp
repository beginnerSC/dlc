#include <gtest/gtest.h>
#include "dlc_core/dp.h"

TEST(DpTest, CanJump) {
    // Test case 1: Can reach the end
    std::vector<int> nums1 = {2, 3, 1, 1, 4};
    EXPECT_EQ(canJump(nums1), true);
    
    // Test case 2: Cannot reach the end (blocked by zero)
    std::vector<int> nums2 = {3, 2, 1, 0, 4};
    EXPECT_EQ(canJump(nums2), false);
    
    // Additional test cases
    std::vector<int> nums3 = {0};  // Single element (already at end)
    EXPECT_EQ(canJump(nums3), true);
    
    std::vector<int> nums4 = {2, 0, 0};  // Can jump over zeros
    EXPECT_EQ(canJump(nums4), true);
    
    std::vector<int> nums5 = {1, 0, 1, 0};  // Cannot reach the end
    EXPECT_EQ(canJump(nums5), false);
}

TEST(DpTest, UniquePaths) {
    // Test case 1: m = 3, n = 7
    EXPECT_EQ(uniquePaths(3, 7), 28);
    
    // Test case 2: m = 3, n = 2
    EXPECT_EQ(uniquePaths(3, 2), 3);
    
    // Additional test cases
    EXPECT_EQ(uniquePaths(1, 1), 1);  // Single cell grid
    EXPECT_EQ(uniquePaths(2, 2), 2);  // 2x2 grid
}

TEST(DpTest, MaximalSquare) {
    std::vector<std::vector<char>> mat1, mat2, mat3;

    mat1 = {
        {'1','0','1','0','0'},
        {'1','0','1','1','1'},
        {'1','1','1','1','1'},
        {'1','0','0','1','0'}
    };
    EXPECT_EQ(maximalSquare(mat1), 4);

    mat2 = {
        {'0','1'},
        {'1','0'}
    };
    EXPECT_EQ(maximalSquare(mat2), 1);

    mat3 = {{'0'}};
    EXPECT_EQ(maximalSquare(mat3), 0);
}

TEST(DpTest, WordBreakAB) {
    // Test basic word break case.
    std::string s = "a";
    std::vector<std::string> wordDict = {"b"};
    EXPECT_EQ(wordBreak(s, wordDict), false);
    EXPECT_EQ(wordBreak1(s, wordDict), false);
}

TEST(DpTest, WordBreakBasicCase) {
    // Test basic word break case.
    std::string s = "leetcode";
    std::vector<std::string> wordDict = {"leet", "code"};
    EXPECT_EQ(wordBreak(s, wordDict), true);
    EXPECT_EQ(wordBreak1(s, wordDict), true);
}

TEST(DpTest, WordBreakNoBreakPossible) {
    // Test when word break is not possible.
    std::string s = "catsandog";
    std::vector<std::string> wordDict = {"cats", "dog", "sand", "and", "cat"};
    EXPECT_EQ(wordBreak(s, wordDict), false);
    EXPECT_EQ(wordBreak1(s, wordDict), false);
}

TEST(DpTest, WordBreakReusableWords) {
    // Test with reusable words.
    std::string s = "applepenapple";
    std::vector<std::string> wordDict = {"apple", "pen"};
    EXPECT_EQ(wordBreak(s, wordDict), true);
    EXPECT_EQ(wordBreak1(s, wordDict), true);
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