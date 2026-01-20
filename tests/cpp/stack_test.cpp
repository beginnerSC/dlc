#include <gtest/gtest.h>
#include "dlc_core/stack.h"

TEST(StackTest, IsValid) {
    EXPECT_EQ(isValid("()"),    true);
    EXPECT_EQ(isValid("()[]{}"), true);
    EXPECT_EQ(isValid("(]"),    false);
    EXPECT_EQ(isValid("([])"),  true);
    EXPECT_EQ(isValid("([)]"),  false);
    EXPECT_EQ(isValid("]"),     false);
}