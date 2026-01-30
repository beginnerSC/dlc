#include "dlc_core/array.h"
#include <vector>
#include <ranges>
#include <unordered_map>
#include <string>
#include <algorithm>    // std::max
#include <limits>

int maxSubArray(std::vector<int>& nums) {   // 53. Maximum Subarray

    // python 的 res = cur_max = float('-inf') 在這裡不能用，
    // 因為一開始 cur_max = -std::numeric_limits<int>::min()，如果 n < 0，迴圈裡的 (cur_max + n) 會變成很大的正數

    int res = nums[0];
    int cur_max = nums[0];

    for (int n : nums | std::views::drop(1)) {
        cur_max = std::max(cur_max + n, n);
        res = std::max(cur_max, res);
    }
    return res;
}

int lengthOfLongestSubstring(std::string s) {   // 3. Longest Substring Without Repeating Characters

    // 標準作法：用雙指標 (left, right) 和一個 char to latest index map 取代 set + queue

    if (s.empty()) {
        return 0;
    }
    std::unordered_map<char, int> d = {{s[0], 0}};
    int left = 0;   // in the below loop, j is right
    int res = 1;

    for (int j=1 ; j<s.size() ; ++j) {
        if (d.contains(s[j]) && d[s[j]]>=left) {
            left = d[s[j]] + 1;
        }
        d[s[j]] = j;
        res = std::max(j-left+1, res);
    }
    return res;
}

std::vector<int> productExceptSelf(std::vector<int>& nums) {    // 238. Product of Array Except Self
    int n = nums.size(); 
    std::vector<int> prefix(n, 1), suffix(n, 1), res(n, 1);

    for(int i=0 ; i<n-1 ; ++i) {
        prefix[i+1] = nums[i]*prefix[i];
    }
    for(int i=n-1 ; i>0 ; --i) {
        suffix[i-1] = nums[i]*suffix[i];
    }
    int i=0;
    for (auto [p, s] : std::views::zip(prefix, suffix)) {
        res[i++] = p*s;
    }
    return res;
}