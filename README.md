# dlc

![2026](yearly_heatmaps/2026.png?ts=10022025) 
![2025](yearly_heatmaps/2025.png?ts=10022025) 

* Longest palindromic substring given $s = \{a_j\}$: 

```python

# Accepted answer modified from 647

def longestPalindrome(self, s: str) -> str:
    n = len(s)

    def expand(l, r):
        while l>=0 and r<n and s[l]==s[r]: 
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
```
```cpp
// Same answer, C++ version
// Same as 647, there is a linear time Manacher's Algorithm
// This solution has space complexity O(n) which can be reduced to O(1) if expand doesn't return anything but changes a max_len and start of substring

#include <string>
#include <utility>
#include <ranges>

string longestPalindrome(string s) {
    int n = s.size();
    auto expand = [&](int l, int r){
        while (l>=0 && r<n && s[l]==s[r]) {
            l -= 1;
            r += 1;
        }
        return s | std::views::drop(l+1) | std::views::take(r-l-1) | std::ranges::to<std::string>();
    };

    std::string best = "";
    
    for (int i=0 ; i<n ; ++i) {
        std::string odd = expand(i, i);
        if (odd.size() > best.size()) {
            best = std::move(odd);
        }
        std::string even = expand(i, i+1);
        if (even.size() > best.size()) {
            best = std::move(even);
        }
    }
    return best;
}
```
* Maximal square given the grid m
    * shape(i, j) = (k, l) if (shape(i-1, j)==(k-1, l) && shape(i, j-1)==(k, l-1) && m(i, j)==1) this is not right. should take min of shape(i-1, j).first and shape(i, j-1).first, and same for second. 
    * also the question is asking for square, not rectangle
* Jump game
    * base case: if a[0] + 2 > a.size() then true. if a[0]==0 and a.size() > 1 then false
```python
# dp solution, O(n^2), working but slow

def canJump(nums):
    @cache
    def dp(j):
        if nums[j]==0 and len(nums) - j > 1:
            return False
        elif j==(len(nums) - 1):
            return True
        else:
            return any(dp(j+i) for i in range(nums[j], 0, -1) if j+i<len(nums))     # reverse or otherwise time limit exceeded

    return dp(0)

# failed greedy attempt: [2,5,0,0]

def canJump(nums: List[int]) -> bool:
    
    @cache
    def dp(j):
        if nums[j]==0 and len(nums) - j > 1:
            return False
        elif j==(len(nums) - 1):
            return True
        else:
            return dp(j+nums[j]) if j + nums[j] < len(nums) else True

    return dp(0)

```
* Maximum Length of Repeated Subarray
    * make a 2d table of true and false. count longest true sequence along the main diagonal 
* Longest Common Subsequence
    * if a[0]==b[0] return 1+lcs(a[1:], b[1:]). Otherwise return max(lcs(a, b[1:]), lcs(a[1:], b))
* Palindromic Substrings
    * for i in range(n): if is_palindromic(s[:i]) then count += (1+countStrings(s[i:]))
    * base case: if len(s)==1: return 1
```python

# Accepted solution, O(n^2) time, O(n^2) space
# 記下所有 palindromic substring indices (i, j), 
# 一開始是 [(0, 0), (1, 1), ..., (0, 1), (1, 2), ...]
# pop index (i, j) 往兩邊長，同時檢查 s[i-1]==s[j+1]

# 這樣寫是 DFS，每次拿一個 substr 來 expand 到不能再 expand 為止
# 如果 popleft 會變成 BFS，每次 expand 所有 substr 一步

def countSubstrings(s):
    n = len(s)
    q = deque([(i, i) for i in range(n)] + [(i, i+1) for i, c in enumerate(s[:-1]) if s[i]==s[i+1]])
    count = len(q)
    while len(q):
        i, j = q.pop()
        if i>0 and j<n-1 and s[i-1]==s[j+1]:
            q.append((i-1, j+1))
            count += 1

    return count 

# AI answer, O(n^2) time, O(1) space
# There is a linear time Manacher's Algorithm

def countSubstrings(s):
    def expand(l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    
    return sum(expand(i, i) + expand(i, i + 1) for i in range(len(s)))

```
```cpp

// AI answer in C++

int countSubstrings(string s) {
    int n = s.size();
    auto expand = [&](int l, int r){
        int count = 0;
        while (l>=0 && r<n && s[l]==s[r]) {
            count += 1;
            l -= 1;
            r += 1;
        }
        return count;
    };

    int count = 0;
    for (int i=0 ; i<n ; ++i)
        count += expand(i, i);

    for (int i=0 ; i<n-1 ; ++i)
        count += expand(i, i+1);
    
    return count;
}

```

* Maximum Product of Three Numbers
    * only the 5 numbers with the largest magnitudes matter
    * they can be 5+, 4+1-, 3+2-, ..., where + includes 0
    * case by case, it can be shown that max(M1*M2*M3, M1*m1*m2) is the answer

* Valid Parentheses

```python
from collections import deque

def isValid(s):     # 20
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
```
* Product of Array Except Self (238)
    * The prefix/suffix pattern: Everything comes before and after the array
    * Questions related to this pattern: 42, 303, 560, 1991, 123

```py

from itertools import accumulate

def productExceptSelf(nums):

    left = list(accumulate([1] + nums[:-1], lambda x, y: x*y))
    right = list(accumulate((nums[1:] + [1])[::-1], lambda x, y: x*y))[::-1]

    return [l*r for l, r in zip(left, right)]
```
```py 

# My segment tree solution in 2020 (linear time, linear space):
# 
# 1. Build a b-tree with numbers on the leaves  
# 2. Bottom up put products in the nodes:                   [[24], [2, 12], [ 1,  2, 3, 4]]
# 3. Swap all sibling nodes:                                [[24], [12, 2], [ 2,  1, 4, 3]]
# 4. Top down (but skip root) multiply the nodes together:  [[24], [12, 2], [24, 12, 8, 6]]

import numpy as np

def productExceptSelf(nums):
    n = len(nums)
    m = 2**(floor(log(n, 2)) + 1)
    a = np.ones(2*m-1, dtype=int)
    a[m-1:m-1+n] = nums

    for i in range(m-2, 0, -1):
        a[i] = a[2*i+1]*a[2*i+2]

    for i in range(1, len(a), 2):
        a[i], a[i+1] = a[i+1], a[i]

    for i in range(1, len(a)):
        a[i] *= a[(i-1)//2]

    return a[m-1:m-1+n]
```


## vcpkg + GoogleTest

* [One time initial vcpkg setup](https://learn.microsoft.com/en-us/vcpkg/get_started/get-started?pivots=shell-cmd)
    * `git clone https://github.com/microsoft/vcpkg.git`
    * `cd vcpkg && bootstrap-vcpkg.bat`
    * `set "VCPKG_ROOT=C:\path\to\vcpkg"`
    * `set PATH=%VCPKG_ROOT%;%PATH%`
    * In project root `vcpkg new --application`
        * In `vcpkg-configuration.json`, the `baseline` in `default-registry` is the HEAD commit of the vcpkg registry at the time running `vcpkg new --application`
    * The `CMakePresets.json` in this guide has `"generator": "Ninja",` which should be replaced by the default generator in the current platform
        * `cmake --help` to check
* To configure cmake and build and run gtest: 
    * Run `cnb` if not using VS Code,
        * Comment out `cmake --preset=vcpkg` to skip repeated config step
        * `cmake --preset=vcpkg` does what `cmake -S . -B build` does which is to configure cmake
        * `cd build & ctest` also runs the test but I like gtest output format more
        * CTest looks for `CTestTestfile.cmake` which is in `build`, as CTest is included and enabled in project root's `CMakeLists.txt`
    * `F5` if using VS Code
        * In `.vscode/launch.json`, use `"preLaunchTask": "CMake: build"` instead of `"preLaunchTask": "CMake: config and build"` to skip repeated config step
    * When to reconfigured: 
        * New cpp/h files added
        * `build` folder deleted, clean rebuild
* `vcpkg add port fmt` to add the `fmt` library to C++ dependencies
* TODO: upgrade poetry (which will break all other projects) and add a `build.py`
    * AI says I can run `poetry config --migrate` to fix `pyproject.toml`? 

### Notes

* Currently this project has an examples folder compiled but the executable is not run by `cnb.bat` nor `.vscode/launch.json`
* AI recommends to keep both examples and (not yet created) docs folders and have docs reference examples so that docs is synced
    * Look into sphinx `literalinclude` and `sphinx-gallery`
    * Examples can be smoked-tested in CI (build and optionally run with a CMake toggle `BUILD_EXAMPLES`) to ensure docs stay accurate