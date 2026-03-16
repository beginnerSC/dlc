from typing import List

def maximumProduct(nums: List[int]) -> int:
    """628. Maximum Product of Three Numbers"""
    
    nums = sorted(nums)

    M1 = nums[-1]
    M2 = nums[-2]
    M3 = nums[-3]

    m1 = nums[0]
    m2 = nums[1]

    return max(M1*m1*m2, M1*M2*M3)