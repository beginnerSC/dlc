#include <unordered_map>
#include <algorithm>
#include <string>
#include <vector>

namespace rg = std::ranges;

std::string longestPalindrome(std::string s) {  // 5. Longest Palindromic Substring
    auto expand = [&](int i, int j){
        int max_len = 0;
        while (i>=0 && j<s.size() && s[i]==s[j]) {
            max_len = j-i+1;
            i -= 1;
            j += 1;
        }
        return std::pair<int, int>({i+1, max_len});
    };

    int best_pos = 0, max_len = 0;

    for (size_t i=0 ; i<s.size() ; ++i) {
        auto [pos, len] = expand(i, i);
        if (len > max_len) {
            best_pos = pos;
            max_len = len;
        }
    }
    for (size_t i=0 ; i<s.size() ; ++i) {
        auto [pos, len] = expand(i, i+1);
        if (len > max_len) {
            best_pos = pos;
            max_len = len;
        }
    }
    return s.substr(best_pos, max_len);
}

std::string reverseWords(std::string s) {   // 151. Reverse Words in a String
    std::vector<std::string> words = {""};
    int n_words = 1;

    for (char c : s) {
        if (c != ' ') {
            words[n_words - 1] += c;
        } else {    // c is the space charactor

            if (words[n_words - 1] != "") {
                words.push_back("");
                n_words += 1;
            }
        }
    }
    if (words[n_words - 1]=="") {
        words.pop_back();
        n_words -= 1;
    }
    std::string res = "";
    for (int j=n_words-1 ; j>=0 ; --j) {
        res += words[j];
        if (j!=0) {
            res += " ";
        }
    }
    return res;
}

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