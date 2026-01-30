from itertools import accumulate
from typing import List
from collections import deque

def lengthOfLongestSubstring(s: str) -> int:
    """3. Longest Substring Without Repeating Characters"""

    # 類似 53. Maximum Subarray，用一個 running max 記下以當前字元結尾的 lengthOfLongestSubstring
    # 但同時存一個 set 和一個 queue 用來計算 running max

    if not s:
        return 0
        
    q = deque(s[:1])
    set_q = set(s[:1])
    cur_max = res = 1
    
    for c in s[1:]:
        while c in set_q:
            cur_max -= 1
            popped = q.popleft()
            set_q.remove(popped)
            
        cur_max += 1
        q.append(c)
        set_q.add(c)
        
        res = max(res, cur_max)

    return res

def lengthOfLongestSubstring1(s):
    """3. Longest Substring Without Repeating Characters"""
    
    # 標準作法：用雙指標 (left, right) 和一個 char to latest index map 取代 set + queue

    if not s:
        return 0

    res = 1
    left = 0          # in the loop below j+1 is right
    d = {s[0]: 0}
    
    for j, c in enumerate(s[1:]):
        if c in d and d[c] >= left:
            left = d[c]+1
        d[c] = j+1
        
        res = max(j-left+2, res)
    return res


def maxSubArray(nums: List[int]) -> int:
    """53. Maximum Subarray"""
    res = cur_max = float('-inf')
    for n in nums:
        cur_max = max(cur_max + n, n)
        res = max(cur_max, res)
    return res


def productExceptSelf(nums: List[int]) -> List[int]:
    """238. Product of Array Except Self"""
    # The prefix/suffix pattern: Everything comes before and after the array
    # Questions related to this pattern: 42, 303, 560, 1991, 123
    left = list(accumulate([1] + nums[:-1], lambda x, y: x*y))
    right = list(accumulate((nums[1:] + [1])[::-1], lambda x, y: x*y))[::-1]
    
    return [l*r for l, r in zip(left, right)]
