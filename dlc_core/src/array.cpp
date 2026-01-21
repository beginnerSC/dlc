#include "dlc_core/array.h"
#include <vector>
#include <ranges>
#include <functional>
#include <print>

std::vector<int> productExceptSelf(std::vector<int>& nums) {
    std::println("{}", std::ranges::fold_left(nums, 1, std::multiplies{}));
}