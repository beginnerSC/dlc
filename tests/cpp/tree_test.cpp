#include <gtest/gtest.h>
#include <dlc_core/tree.h>

TEST(MathTest, LevelOrder) {
    // TreeNode n15(15), n7(7), n9(9), n20(20, &n15, &n7), root(3, &n9, &n20);
    TreeNode* root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
    EXPECT_EQ(levelOrder(root), {{3}, {9, 20}, {15, 17}});
}