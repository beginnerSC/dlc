#include <vector>
#include <algorithm>
#include <unordered_map>
#include <ranges>
#include <string>
#include <functional>

namespace rg = std::ranges;
namespace vs = std::views;

bool canJump(std::vector<int>& nums) {
    size_t size = nums.size();
    std::function<bool(size_t)> dp = [&](size_t j){
        if (j!=size-1 && nums[j]==0) {
            return false;
        } else if (j!=size-1 && (nums[j]+j) >= size-1) {
            return true;
        } else {
            for (size_t i=j ; i>0 ; --j) {
                if (dp(j+i)) {
                    return dp(j+i);
                }
            }
            return false;
        }
    };
    return dp(0);
}

int uniquePaths(int m, int n) {     // 62. Unique Paths

    std::vector<std::vector<int>> dp(m, std::vector<int>(n));

    for (int i=0 ; i<m ; ++i) {
        for (int j=0 ; j<n ; ++j) {
            dp[i][j] = (i==0 || j==0) ? 1 : (dp[i-1][j] + dp[i][j-1]);
        }
    }
    return dp[m-1][n-1];
}

int maximalSquare(std::vector<std::vector<char>>& matrix) {     // 221. Maximal Square
    int m = matrix.size();
    int n = matrix[0].size();
    std::vector<std::vector<int>> dp(m, std::vector<int>(n));

    int max_len = 0;
    for (int i=0 ; i<m ; ++i) {
        for (int j=0 ; j<n ; ++j) {
            if (i==0 || j==0) {
                dp[i][j] = (matrix[i][j]=='0') ? 0 : 1;
            } else if (matrix[i][j] == '0'){
                dp[i][j] = 0;
            } else {
                dp[i][j] = 1 + std::min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
            max_len = std::max(dp[i][j], max_len);
        }
    }
    return max_len*max_len;
}


bool wordBreak1(std::string s, std::vector<std::string>& wordDict) {     // 139. Word Break

    // Hasing index version with substr. rg::to makes copies which is a waste of time 
    // Use size_t instead of int to avoid compiler warning

    std::unordered_map<size_t, bool> memo = {{s.size(), true}};

    std::function<bool(size_t j)> dp = [&](size_t j){
        if (memo.contains(j)) {
            return memo[j];
        } else {
            bool res = false;
            for (const std::string& word : wordDict) {
                if (s.substr(j).starts_with(word)) {
                    res = dp(j + word.size());
                    if (res) {
                        break;
                    }
                }
            }
            memo[j] = res;
            return res;
        }
    };
    return dp(0);
}

bool wordBreak(std::string s, std::vector<std::string>& wordDict) {     // 139. Word Break
    std::unordered_map<std::string, bool> memo = {{"", true}};

    std::function<bool(const std::string& s)> dp = [&](const std::string& s){
        if (memo.contains(s)) {
            return memo[s];
        } else {
            bool res = false;
            for (const std::string& word : wordDict) {
                if (s.starts_with(word)) {
                    res = dp(s | vs::drop(word.size()) | rg::to<std::string>());
                    if (res) {
                        break;
                    }
                }
            }
            memo[s] = res;
            return res;
        }
    };
    return dp(s);
}

int longestCommonSubsequence(std::string text1, std::string text2) {    // 1143. Longest Common Subsequence
    std::vector<std::vector<int>> dp(text1.size(), std::vector<int>(text2.size(), 0));

    for (int i=0 ; i<text1.size() ; ++i) {
        if (text1[i] == text2[0]) {
            dp[i][0] = 1;
        }
        if (i>0) {
            dp[i][0] = std::max(dp[i][0], dp[i-1][0]);
        }
    }
    for (int j=0 ; j<text2.size() ; ++j) {
        if (text1[0] == text2[j]) {
            dp[0][j] = 1;
        }
        if (j>0) {
            dp[0][j] = std::max(dp[0][j], dp[0][j-1]);
        }
    }
    int res = std::max(dp[0][text2.size()-1], dp[text1.size()-1][0]);
    for (int i=1 ; i<text1.size() ; ++i) {
        for (int j=1 ; j<text2.size() ; ++j) {
            if (text1[i] == text2[j]) {
                dp[i][j] = dp[i-1][j-1] + 1;
                res = std::max(dp[i][j], res);
            } else {
                dp[i][j] = std::max(dp[i][j-1], dp[i-1][j]);
            }
        }
    }
    return res;
}

int findLength(std::vector<int>& nums1, std::vector<int>& nums2) {  // 718. Maximum Length of Repeated Subarray

    std::vector<std::vector<int>> dp(nums1.size(), std::vector<int>(nums2.size()));

    for (int i=0 ; i<nums1.size() ; ++i) {
        for (int j=0 ; j<nums2.size() ; ++j) {
            dp[i][j] = (nums1[i]==nums2[j]) ? 1 : 0;
        }
    }
    for (int i=1 ; i<nums1.size() ; ++i) {
        for (int j=1 ; j<nums2.size() ; ++j) {
            if (dp[i][j] == 1) {
                dp[i][j] += dp[i-1][j-1];
            }
        }
    }
    int max = 0;
    for (int i=0 ; i<nums1.size() ; ++i) {
        for (int j=0 ; j<nums2.size() ; ++j) {
            max = std::max(max, dp[i][j]);
        }
    }
    
    return max;
}

int rob(std::vector<int>& nums) {   // 198. House Robber
    int pre = 0;
    int cur = nums.front();
    for (size_t i = 1; i < nums.size(); ++i) {
        int temp = cur;
        cur = std::max(cur, pre + nums[i]);
        pre = temp;
    }
    return cur;
}

int coinChange(std::vector<int>& coins, int amount) {   // 322. Coin Change
    std::unordered_map<int, int> dp;
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

int climbStairs(int n) {   // 70. Climbing Stairs
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