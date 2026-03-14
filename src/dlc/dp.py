from functools import cache
from typing import List
import numpy as np


def coinChange(coins: List[int], amount: int) -> int:
    """322. Coin Change"""
    @cache
    def dp(amount):
        if amount < 0:
            return float('inf')
        elif amount == 0:
            return 0
        else:
            return 1 + min(dp(amount - coin) for coin in coins)
    
    res = dp(amount)
    
    return -1 if res==float('inf') else res

def maximalSquare(matrix: List[List[str]]) -> int:
    """221. Maximal Square"""
    
    m, n = len(matrix), len(matrix[0])
    matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]

    max_len = max([matrix[0][j] for j in range(n)] + [matrix[i][0] for i in range(m)])
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                max_len = max(max_len, matrix[i][j])

    return max_len**2

def rob(nums: List[int]) -> int:
    """198. House Robber"""

    if len(nums)==1:
        return nums[0]
    else:
        m = [0, nums[0]] + [0 for _ in nums[1:]]
        for j, n in enumerate(nums[1:]):
            m[j+2] = max(m[j] + n, m[j+1])

        return m[-1]

@cache
def fib(n: int) -> int:
    """509. Fibonacci Number"""
    
    return n if (n<2) else (fib(n-1) + fib(n-2))

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
