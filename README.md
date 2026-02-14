# Daily LeetCode Challenge

![2026](yearly_heatmaps/2026.png?ts=10022025) 
![2025](yearly_heatmaps/2025.png?ts=10022025) 

This is a repo to store my solutions to LeetCode questions, in both C++ and Python. 

* TODO
    * Bsearch 有一種每圈迴圈多推一步的作法
    * Many (all?) 2D DP can be done with 1D vector
    * 718 Maximum Length of Repeated Subarray has a $O(N \log N)$ solution. AI mentioned binary search + rolling hash, and sliding window
    * 139 Word Break in C++: 
        * Keep notes on C++ lambda recursion: Lambda 在定義完成前，其變數名稱（如 auto func）對 Lambda 內部是不可見的。可以用 `std::function`
        * Local static is not needed! 

## Project Structure

```
dlc/
├── cpp/                          # C++ source code
│   ├── include/dlc_core/         # Header files
│   │   └── array.h
│   ├── src/                      # Implementation files
│   │   └── array.cpp
│   ├── bindings/                 # pybind11 bindings
│   │   └── dlc_bindings.cpp
│   └── CMakeLists.txt
├── src/dlc/                      # Python package
│   ├── __init__.py
│   └── array.py
├── tests/
│   ├── cpp/                      # C++ tests
│   │   └── array_test.cpp
│   └── python/                   # Python tests
│       └── test_array.py
├── examples/cpp/                 # C++ examples
├── yearly_heatmaps/
├── CMakeLists.txt               # Root CMake configuration
├── pyproject.toml               # Poetry configuration
├── build.py                     # Build script
└── upgrade_package.bat          # Package upgrade helper
```

## Building

### C++ with CMake and GTest

Run tests:
```batch
cnb.bat
```

### Python Package with Poetry

1. Build the wheel:
```batch
poetry build
```

2. Install/upgrade the package:
```batch
upgrade_package.bat
```

---

## Leetcode Solutions

Python solutions are in `src/dlc/` with tests in `tests/python/`.

* Longest palindromic substring given $s = \{a_j\}$: 
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
* Palindromic Substrings
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
* Maximal square given the grid m
    * shape(i, j) = (k, l) if (shape(i-1, j)==(k-1, l) && shape(i, j-1)==(k, l-1) && m(i, j)==1) this is not right. should take min of shape(i-1, j).first and shape(i, j-1).first, and same for second. 
    * also the question is asking for square, not rectangle
* Maximum Length of Repeated Subarray (718)
    * make a 2d table of true and false. count longest true sequence along the main diagonal 
```py
# Seemingly working but memory limit exceeded

def findLength(nums1, nums2):
    m = np.array([[1 if (n==m) else 0 for n in nums2] for m in nums1])
    print(np.array(m))

    @cache
    def count(i, j):
        res = 1
        if i<len(nums1)-1 and j<len(nums2)-1 and m[i+1][j+1]==1:
            res += count(i+1, j+1)
            
        return res

    max_len = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if m[i][j]==1:
                max_len = max(count(i, j), max_len)

    return max_len
```
* Longest Common Subsequence
    * if a[0]==b[0] return 1+lcs(a[1:], b[1:]). Otherwise return max(lcs(a, b[1:]), lcs(a[1:], b))
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