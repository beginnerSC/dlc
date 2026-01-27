#include <vector>
#include <algorithm>
#include <functional>

int maximumProduct(std::vector<int>& nums) {    // https://leetcode.com/problems/maximum-product-of-three-numbers/description/

    std::partial_sort(nums.begin(), nums.begin() + 3, nums.end(), std::greater<int>());

    int M1 = nums[0];
    int M2 = nums[1];
    int M3 = nums[2];

    std::partial_sort(nums.begin(), nums.begin() + 2, nums.end(), std::less<int>());

    int m1 = nums[0];
    int m2 = nums[1];

    return std::max(M1*M2*M3, M1*m1*m2);
}