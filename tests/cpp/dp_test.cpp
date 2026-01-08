#include <gtest/gtest.h>
#include <dlc_core/dp.h>

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