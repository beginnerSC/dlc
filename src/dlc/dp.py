from functools import cache
from typing import List
import numpy as np

def findLength(nums1: List[int], nums2: List[int]) -> int:
    """718. Maximum Length of Repeated Subarray"""
    
    m = np.array([[1 if (n==m) else 0 for n in nums2] for m in nums1])

    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if m[i, j] == 1:
                m[i, j] += m[i-1, j-1]

    return int(np.max(m))

def wordBreak(s: str, wordDict: List[str]) -> bool:
    """139. Word Break"""
    @cache
    def dp(s):
        if len(s) == 0:
            return True
        return any([dp(s[len(word):]) for word in wordDict if s.startswith(word)])
    
    return dp(s)

def canJump(nums: List[int]) -> bool:
    """55. Jump Game"""
    # base case: if a[0] + 2 > a.size() then true. if a[0]==0 and a.size() > 1 then false
    # dp solution, O(n^2), working but slow
    # failed greedy attempt: [2,5,0,0]
    @cache
    def dp(j):
        if nums[j] == 0 and len(nums) - j > 1:
            return False
        elif j == (len(nums) - 1):
            return True
        else:
            return any(dp(j+i) for i in range(nums[j], 0, -1) if j+i < len(nums))     # reverse or otherwise time limit exceeded
    
    return dp(0)
