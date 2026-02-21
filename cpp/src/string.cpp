#include <unordered_map>
#include <algorithm>
#include <string>

namespace rg = std::ranges;

bool isAnagram(std::string s, std::string t) {      // 242. Valid Anagram
    rg::sort(s);
    rg::sort(t);
    
    return s==t;
}

bool isAnagram1(std::string s, std::string t) {     // 242. Valid Anagram
    std::unordered_map<char, int> s_count, t_count;
    
    for (char c : s) {
        s_count[c] += 1;
    }
    for (char c : t) {
        t_count[c] += 1;
    }
    return s_count == t_count;
}