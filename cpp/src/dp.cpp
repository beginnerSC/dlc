#include <vector>
#include <algorithm>
#include <unordered_map>
#include <ranges>

int maxSubArray(std::vector<int>& nums) { // https://leetcode.com/problems/maximum-subarray/description/
    int res = nums[0];
    int cur_max = nums[0];
    for (int n : nums | std::views::drop(1)) {
        cur_max = std::max(cur_max + n, n);
        res = std::max(cur_max, res);
    }
    return res;
}

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
        dp[amount] = std::ranges::min(num_coins);
        return dp[amount];
    }
}

int climbStairs(int n) {   // https://leetcode.com/problems/climbing-stairs/
  if (n < 3){
    return n;
  } else {
    int pre = 1;
    int cur = 2;
    for (int j=3 ; j<n+1 ; ++j) {
      int tmp = cur;
      cur += pre;
      pre = tmp;
    }
    return cur;
  }
}