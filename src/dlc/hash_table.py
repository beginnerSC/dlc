from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """217. Contains Duplicate"""

    return len(nums) != len(set(nums))

def twoSum(nums, target):
    """1. Two Sum"""

    d = dict()
    for j, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], j]
        else: 
            d[n] = j