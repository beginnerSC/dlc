#include <vector>
#include <algorithm>
#include <unordered_map>
#include <ranges>

namespace rg = std::ranges;
namespace vs = std::views;

int findLength(std::vector<int>& nums1, std::vector<int>& nums2) {

    std::vector<std::vector<int>> m(nums1.size(), std::vector<int>(nums2.size()));

    for (int i=0 ; i<nums1.size() ; ++i) {
        for (int j=0 ; j<nums2.size() ; ++j) {
            m[i][j] = (nums1[i]==nums2[j]) ? 1 : 0;
        }
    }
    for (int i=1 ; i<nums1.size() ; ++i) {
        for (int j=1 ; j<nums2.size() ; ++j) {
            if (m[i][j] == 1) {
                m[i][j] += m[i-1][j-1];
            }
        }
    }
    int max = 0;
    for (int i=0 ; i<nums1.size() ; ++i) {
        for (int j=0 ; j<nums2.size() ; ++j) {
            max = std::max(max, m[i][j]);
        }
    }
    
    return max;
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
        dp[amount] = rg::min(num_coins);
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