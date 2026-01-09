#include <gtest/gtest.h>
#include <dlc_core/tree.h>

TEST(TreeTest, LevelOrder) {
    TreeNode* root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
    // TreeNode n15(15), n7(7), n9(9), n20(20, &n15, &n7), root(3, &n9, &n20);  // alternative one line tree construction

    std::vector<std::vector<int>> res = {{3}, {9, 20}, {15, 7}};
    EXPECT_EQ(levelOrder(root), res);

    // have to invoke constructor with parentheses or otherwise double braces in a function call is ambiguous
    EXPECT_EQ(levelOrder(root), std::vector<std::vector<int>>({{3}, {9, 20}, {15, 7}}));

    //// doesn't compile
    // void test(std::vector<std::vector<int>>&& v) { }
    // test(std::vector<std::vector<int>>{{3}, {9, 20}, {15, 7}});
}