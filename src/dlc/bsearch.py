from typing import List

def search(nums: List[int], target: int) -> int:
    """704. Binary Search"""
    
    l = 0
    r = len(nums)-1

    while r-l > 1:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m
        else:           # nums[m] > target
            l = m

    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    else:
        return -1
