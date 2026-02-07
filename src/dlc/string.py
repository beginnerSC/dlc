import re
from collections import Counter, deque

def reverseWords(s: str) -> str:
    """151. Reverse Words in a String"""

    return ' '.join(re.sub('[ ]+', ' ', s.strip()).split(' ')[::-1])

def isAnagram(s: str, t: str) -> bool:
    """242. Valid Anagram"""

    return sorted(s) == sorted(t)

def isAnagram_counter(s: str, t: str) -> bool:
    """242. Valid Anagram (Counter)"""

    return Counter(s) == Counter(t)

def longestPalindrome(s: str) -> str:
    """5. Longest Palindromic Substring"""
    # Longest palindromic substring given $s = \{a_j\}$
    # Accepted answer modified from 647

    n = len(s)
    
    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    best = ""
    for i in range(n):
        odd = expand(i, i)
        if len(odd) > len(best):
            best = odd
        
        even = expand(i, i+1)
        if len(even) > len(best):
            best = even
    
    return best

def countSubstrings(s: str) -> int:
    """647. Palindromic Substrings"""
    # Palindromic Substrings
    # for i in range(n): if is_palindromic(s[:i]) then count += (1+countStrings(s[i:]))
    # base case: if len(s)==1: return 1
    # Accepted solution, O(n^2) time, O(n^2) space
    # 記下所有 palindromic substring indices (i, j), 
    # 一開始是 [(0, 0), (1, 1), ..., (0, 1), (1, 2), ...]
    # pop index (i, j) 往兩邊長，同時檢查 s[i-1]==s[j+1]

    # 這樣寫是 DFS，每次拿一個 substr 來 expand 到不能再 expand 為止
    # 如果 popleft 會變成 BFS，每次 expand 所有 substr 一步

    # AI answer, O(n^2) time, O(1) space
    # There is a linear time Manacher's Algorithm

    def expand(l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

    return sum(expand(i, i) + expand(i, i + 1) for i in range(len(s)))

def isValid(s: str) -> bool:
    """20. Valid Parentheses"""

    stack = deque()
    close_to_open = {')': '(', ']': '[', '}': '{'}
    
    for c in s:
        if c in ['(', '[', '{']:    # c is open
            stack.append(c)
        if c in close_to_open:      # c is a close 
            if not stack:
                return False
            else:
                top = stack.pop()
                if top != close_to_open[c]:
                    return False
    
    return (not stack)     # q has to be empty in the end 
