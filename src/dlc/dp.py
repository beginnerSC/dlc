from functools import cache
from typing import List
import numpy as np

def uniquePaths(m: int, n: int) -> int:
    """62. Unique Paths"""
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
    return dp[-1][-1]

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """1143. Longest Common Subsequence"""

    # 其實不需要 keep running max。直接回傳矩陣右下角就可以

    dp = np.array([[(1 if c==d else 0) for c in text2] for d in text1])

    for i in range(1, len(text1)):
        dp[i, 0] = max(dp[i, 0], dp[i-1, 0])

    for j in range(1, len(text2)):
        dp[0, j] = max(dp[0, j], dp[0, j-1])

    res = max(dp[-1, 0], dp[0, -1])
    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            if text1[i] == text2[j]:
                dp[i, j] = dp[i-1, j-1] + 1
                res = max(dp[i, j], res)
            else:
                dp[i, j] = max(dp[i, j-1], dp[i-1, j])

    return int(res)

def findLength(nums1: List[int], nums2: List[int]) -> int:
    """718. Maximum Length of Repeated Subarray"""
    
    dp = np.array([[1 if (n==m) else 0 for n in nums2] for m in nums1])

    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if dp[i, j] == 1:
                dp[i, j] += dp[i-1, j-1]

    return int(np.max(dp))

def wordBreak(s: str, wordDict: List[str]) -> bool:
    """139. Word Break"""
    @cache
    def dp(s):
        if len(s) == 0:
            return True
        return any(dp(s[len(word):]) for word in wordDict if s.startswith(word))
    
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
