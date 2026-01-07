# dlc

![2026](yearly_heatmaps/2026.png?ts=10022025) 
![2025](yearly_heatmaps/2025.png?ts=10022025)

* TODO: Move ohhh here. 
* Maximum subarray given $\{a_j\}$: 
    * $m_n$: Sum of running max subarray 
    * $s_n$: Sum of running max subarray ending $a_n$
    * $m_n = \max(s_{n-1} + a_n, m_{n-1})$
* Longest palindromic substring given $s = \{a_j\}$: 
    * $q_n$: Indeices `(k, l)` of the longest palindromic substring from `s[:n]`
    * $p_n$: Indecies `(i, j)` of the longest palindromic substring ending `s[n-1]`
    * If `s[i-1] == s[n]` then $p_{n+1} = $`(i-1, n)`. See if $q$ should be updated 
    * Also equal to the longest common substring of `s` and `s[::-1]`
* Maximal square given the grid m
    * shape(i, j) = (k, l) if (shape(i-1, j)==(k-1, l) && shape(i, j-1)==(k, l-1) && m(i, j)==1) this is not right. should take min of shape(i-1, j).first and shape(i, j-1).first, and same for second. 
    * also the question is asking for square, not rectangle
* Jump game
    * base case: if a[0] + 2 > a.size() then true. if a[0]==0 and a.size() > 1 then false
* Maximum Length of Repeated Subarray
    * make a 2d table of true and false. count longest true sequence along the main diagonal 
* Longest Common Subsequence
    * if a[0]==b[0] return 1+lcs(a[1:], b[1:]). Otherwise return max(lcs(a, b[1:]), lcs(a[1:], b))
* Palindromic Substrings
    * for i in range(n): if is_palindromic(s[:i]) then count += (1+countStrings(s[i:]))
    * base case: if len(s)==1: return 1
=========================
from functools import cache

class Solution:
    def is_palindromic(self, s):
        return s == s[::-1]

    def countSubstrings(self, s: str) -> int:
        @cache
        def dp(i):
            count = 0
            for i in range(len(s)):
                if self.is_palindromic(s[:i]):
                    count += (1 + dp(s[i:]))
==========================

* Maximum Product of Three Numbers
    * only the 5 numbers with the largest magnitudes matter
    * they can be 5+, 4+1-, 3+2-, ..., where + includes 0
    * case by case, it can be shown that max(M1*M2*M3, M1*m1*m2) is the answer
