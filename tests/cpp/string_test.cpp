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
