#include <string>
#include <stack>
#include <unordered_map>

bool isValid(std::string s) {   // 20. Valid Parentheses
    std::stack<char> stack;
    std::unordered_map<char, char> close_to_open = {{')', '('}, {']', '['}, {'}', '{'}};

    for (char c : s) {
        if (c=='(' || c=='[' || c=='{') {   // c is an open
            stack.push(c);
        } else if (close_to_open.contains(c)) { // c is close
            if (stack.size() && stack.top()==close_to_open[c]) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    return !stack.size();
}