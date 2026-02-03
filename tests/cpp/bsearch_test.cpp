#include <gtest/gtest.h>
#include "dlc_core/bsearch.h"

TEST(BsearchTest, Search) {
    std::vector<int> nums = {-1,0,3,5,9,12};
    int target = 9;
    EXPECT_EQ(search(nums, target), 4);
    
    nums = {-1,0,3,5,9,12};
    target = 2;
    EXPECT_EQ(search(nums, target), -1);
}
