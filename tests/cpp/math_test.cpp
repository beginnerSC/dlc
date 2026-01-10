#include <gtest/gtest.h>
#include "dlc_core/math.h"

TEST(MathTest, MaximumProduct) {
    std::vector<int> nums = {1, 2, 3, 4};
    EXPECT_EQ(maximumProduct(nums), 24);
}