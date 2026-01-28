from itertools import accumulate
from typing import List


def maxSubArray(nums: List[int]) -> int:
    """53. Maximum Subarray"""
    res = cur_max = nums[0]
    for n in nums[1:]:
        cur_max = max(n, cur_max + n)
        res = max(cur_max, res)
    return res


def productExceptSelf(nums: List[int]) -> List[int]:
    """238. Product of Array Except Self"""
    # The prefix/suffix pattern: Everything comes before and after the array
    # Questions related to this pattern: 42, 303, 560, 1991, 123
    left = list(accumulate([1] + nums[:-1], lambda x, y: x*y))
    right = list(accumulate((nums[1:] + [1])[::-1], lambda x, y: x*y))[::-1]
    
    return [l*r for l, r in zip(left, right)]
