#include <gtest/gtest.h>
#include "dlc_core/array.h"

TEST(MathArray, ProductExceptSelf) {
    std::vector<int> nums = {1, 2, 3, 4};
    EXPECT_EQ(productExceptSelf(nums), {24, 12, 8, 6});
}