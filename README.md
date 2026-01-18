# dlc

![2026](yearly_heatmaps/2026.png?ts=10022025) 
![2025](yearly_heatmaps/2025.png?ts=10022025) 

* Longest palindromic substring given $s = \{a_j\}$: 

```python

# modified from 647 answer but result is wrong

def longestPalindrome(s):
    n = len(s)

    def expand(l, r):
        max = 0
        while l>=0 and r<n and s[l]==s[r]: 
            l -= 1
            r += 1
            max += 1

        return l, r

    max = 0
    for i in range(n):
        l, r = expand(i, i)
        if r-l+1 > max:
            max = r-l+1
            res = s[l:r+1]

    for i in range(n-1):
        l, r = expand(i, i+1)
        if r-l+1 > max:
            max = r-l+1
            res = s[l:r+1]

    return res
```
```cpp
// modified from 647 answer but result is wrong

string longestPalindrome(string s) {
    int n = s.size();
    auto expand = [&](int l, int r){
        int max = 0;
        while (l>=0 && r<n && s[l]==s[r]) {
            max += 1;
            l -= 1;
            r += 1;
        }
        return std::pair{l, r};
    };

    int max = 0;
    std::string res = "";
    for (int j=n-1 ; j<=n ; ++j) {
        for (int i=0 ; i<n ; ++i) {
            auto [l, r] = expand(i, i);
            if (r-l+1 > max) {
                res = s | std::views::drop(l) | std::views::take(r-l+1) | std::ranges::to<std::string>();
            }
        }
    }
    return res;
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
# pop index (i, j) 往兩邊長，同時檢察 s[i-1]==s[j+1]

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