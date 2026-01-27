
def twoSum(nums, target):
    """1. Two Sum"""

    d = dict()
    for j, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], j]
        else: 
            d[n] = j