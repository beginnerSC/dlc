# dlc

![heatmap](yearly_heatmaps/2025.png?ts=10022025) 

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