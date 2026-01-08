#include <vector>
#include <algorithm>
#include <unordered_map>

int rob(std::vector<int>& nums) {   // https://leetcode.com/problems/house-robber/
    int pre = 0;
    int cur = nums.front();
    for (size_t i = 1; i < nums.size(); ++i) {
        int temp = cur;
        cur = std::max(cur, pre + nums[i]);
        pre = temp;
    }
    return cur;
}

int coinChange(std::vector<int>& coins, int amount) {   // https://leetcode.com/problems/coin-change/
    static std::unordered_map<int, int> dp;
    if (amount < 0) {
        return -1;
    } else if (amount == 0) {   // trace the code without this branch
        return 0;
    } else if (dp.contains(amount)) {
        return dp[amount];
    } else {
        std::vector<int> num_coins;
        int min = std::numeric_limits<int>::max();
        for (int coin : coins){
            int sub = coinChange(coins, amount - coin);
            if (sub != -1) {
                num_coins.push_back(sub + 1);
            }
        }
        dp[amount] = *std::min_element(num_coins.begin(), num_coins.end());
        return dp[amount];
    }
}