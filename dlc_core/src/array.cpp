#include "dlc_core/array.h"
#include <vector>
#include <ranges>

std::vector<int> productExceptSelf(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> prefix = {1}, suffix = {1};

    for(int i=0 ; i<n-1 ; ++i) {
        prefix.push_back(prefix.back()*nums[i]);
    }
    for(int i=n-1 ; i>0 ; --i) {
        suffix.push_back(suffix.back()*nums[i]);
    }
    std::vector<int> res;
    for (auto [p, s] : std::views::zip(prefix, suffix | std::views::reverse)) {
        res.push_back(p * s);
    }
    return res;
}