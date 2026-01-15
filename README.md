# dlc

![2026](yearly_heatmaps/2026.png?ts=10022025) 
![2025](yearly_heatmaps/2025.png?ts=10022025) 

* Maximum subarray given $\{a_j\}$: 
    * $m_n$: Sum of running max subarray 
    * $s_n$: Sum of running max subarray ending $a_n$
    * $m_n = \max(s_{n-1} + a_n, m_{n-1})$
* Longest palindromic substring given $s = \{a_j\}$: 
    * $q_n$: Indeices `(k, l)` of the longest palindromic substring from `s[:n]`
    * $p_n$: Indecies `(i, j)` of the longest palindromic substring ending `s[n-1]`
    * If `s[i-1] == s[n]` then $p_{n+1} = $`(i-1, n)`. See if $q$ should be updated 
    * Also equal to the longest common substring of `s` and `s[::-1]`
```python
    def longestPalindrome(self, s: str) -> str:

        @cache
        def dp(s):
            if len(s) == 1:
                return (0, 0)
            else: 
                n = len(s)
                i, j = dp(s[:-1])
                if i>1 and j==n-2 and s[n-1]==s[i-1]:
                    return (i-1, j+1)
                else: 
                    ########## ?????????????? ##########
                    pass

        i, j = dp(s)

        return s[i: j]
```
* Maximal square given the grid m
    * shape(i, j) = (k, l) if (shape(i-1, j)==(k-1, l) && shape(i, j-1)==(k, l-1) && m(i, j)==1) this is not right. should take min of shape(i-1, j).first and shape(i, j-1).first, and same for second. 
    * also the question is asking for square, not rectangle
* Jump game
    * base case: if a[0] + 2 > a.size() then true. if a[0]==0 and a.size() > 1 then false
```python
# working but slow

def canJump(nums):
    @cache
    def dp(j):
        if nums[j]==0 and len(nums) - j > 1:
            return False
        elif j==(len(nums) - 1):
            return True
        else:
            return any(dp(j+i) for i in range(nums[j], 0, -1) if j+i<len(nums))     # greedy or otherwise time limit exceeded

    return dp(0)
```
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