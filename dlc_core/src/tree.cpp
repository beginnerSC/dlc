#include <vector>
#include <deque>
#include <dlc_core/tree.h>

std::vector<std::vector<int>> levelOrder(TreeNode* root) {

  if (root==nullptr) return {};

  std::vector<std::vector<int>> res;
  std::deque<TreeNode*> q{root};

  while (!q.empty()){
    std::vector<int> level = {};
    size_t n = q.size();
    for (size_t i=0 ; i<n ; i++) {
      TreeNode* node = q.front(); 
      level.push_back(node->val);
      if (node->left) q.push_back(node->left);
      if (node->right) q.push_back(node->right);
      q.pop_front();
    }
    res.push_back(level);
  }
  return res;
}