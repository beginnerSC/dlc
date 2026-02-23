#include <gtest/gtest.h>
#include "dlc_core/string.h"

TEST(StringTest, IsAnagram) {
    EXPECT_TRUE(isAnagram("anagram", "nagaram"));
    EXPECT_FALSE(isAnagram("rat", "car"));
    EXPECT_TRUE(isAnagram("", ""));
    EXPECT_TRUE(isAnagram("a", "a"));
    EXPECT_FALSE(isAnagram("ab", "a"));
    EXPECT_TRUE(isAnagram("listen", "silent"));
    EXPECT_TRUE(isAnagram("triangle", "integral"));
}

TEST(StringTest, IsAnagram1) {
    EXPECT_TRUE(isAnagram1("anagram", "nagaram"));
    EXPECT_FALSE(isAnagram1("rat", "car"));
    EXPECT_TRUE(isAnagram1("", ""));
    EXPECT_TRUE(isAnagram1("a", "a"));
    EXPECT_FALSE(isAnagram1("ab", "a"));
    EXPECT_TRUE(isAnagram1("listen", "silent"));
    EXPECT_TRUE(isAnagram1("triangle", "integral"));
}

TEST(StringTest, ReverseWords) {
    EXPECT_EQ(reverseWords("the sky is blue"), "blue is sky the");
    EXPECT_EQ(reverseWords("  hello world  "), "world hello");
    EXPECT_EQ(reverseWords("a good   example"), "example good a");
    EXPECT_EQ(reverseWords("a"), "a");
    EXPECT_EQ(reverseWords(""), "");
    EXPECT_EQ(reverseWords("   "), "");
}

TEST(StringTest, LongestPalindrome) {
    // Test case 1: "babad" can return either "bab" or "aba"
    std::string result1 = longestPalindrome("babad");
    EXPECT_TRUE(result1 == "bab" || result1 == "aba");
    EXPECT_EQ(result1.length(), 3);
    
    // Test case 2: "cbbd" should return "bb"
    EXPECT_EQ(longestPalindrome("cbbd"), "bb");
    
    // Additional edge cases
    EXPECT_EQ(longestPalindrome("a"), "a");
    EXPECT_EQ(longestPalindrome("ac"), "a");
    EXPECT_EQ(longestPalindrome("racecar"), "racecar");
    EXPECT_EQ(longestPalindrome("noon"), "noon");
    
    // Another case with even-length palindrome
    std::string result2 = longestPalindrome("abba");
    EXPECT_EQ(result2, "abba");
}
