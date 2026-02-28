#include <unordered_map>
#include <algorithm>
#include <string>
#include <vector>

namespace rg = std::ranges;

int countSubstrings(std::string s) {     // 647. Palindromic Substrings
    int count = 1;
    int max_len_ending_si = 1;
    for (int i=1 ; i<s.size() ; ++i) {
        int tmp = 1;
        for (int j=i ; j>=std::max(i-max_len_ending_si-1, 0) ; --j) {
            if (s[j]==s[i]) {
                ++count;
            }                 
            if (j==i-max_len_ending_si-1) {
                if (s[j]==s[i]) {
                    max_len_ending_si += 2;
                } else if (s[j+1]==s[i]) {
                    max_len_ending_si += 1;
                } else {
                    max_len_ending_si = 1;
                }
            }
        }
    }
    return count;
}

std::string longestPalindrome(std::string s) {  // 5. Longest Palindromic Substring
    int best_pos = 0, max_len = 0;

    auto check = [&](int l, int r){

        while (l>=0 && r<s.size() && s[l]==s[r]) {
            l -= 1;
            r += 1;
        }
        l += 1;
        r -= 1;

        if (r-l+1 > max_len) {    // In AI's clean solution, this block is on the top of the while loop, so that l += 1 and r -= 1 can be avoided
            best_pos = l;
            max_len = r-l+1;
        }
    };
    for (size_t i=0 ; i<s.size() ; ++i) {
        check(i, i);
        check(i, i+1);
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