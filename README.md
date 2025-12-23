# dlc

![heatmap](yearly_heatmaps/2025.png?ts=10022025) 

* TODO: Move ohhh here. 
* Maximum subarray given $\{a_j\}$: 
    * $m_n$: Sum of running max subarray 
    * $s_n$: Sum of running max subarray ending $a_n$
    * $m_n = \max(s_{n-1} + a_n, m_{n-1})$
