#include <utility>
#include <vector>
#include <unordered_map>

std::pair<int, int> twoSum(std::vector<int> nums, int target) {
    std::unordered_map<int, int> d;
    for (size_t i=0 ; i<nums.size() ; ++i) {
        if (d.contains(target - nums[i])) {
            return {d[target - nums[i]], i};
        } else {
            d[nums[i]] = i;
        }
    }
}