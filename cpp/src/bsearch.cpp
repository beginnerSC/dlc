#include "dlc_core/array.h"
#include <vector>

int search(std::vector<int>& nums, int target) {    // 704. Binary Search
    int l = 0;
    int r = nums.size() - 1;

    while (r-l > 1) {
        int m = l + (r-l)/2;
        if (nums[m] == target) {
            return m;
        } else if (nums[m] > target) {
            r = m;
        } else {    // nums[m] < target
            l = m;
        }
    }
    if (nums[l] == target) {
        return l;
    } else if (nums[r] == target) {
        return r;
    } else {
        return -1;
    }
}