#include "dlc_core/array.h"
#include <vector>
#include <ranges>

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