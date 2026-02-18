#include <gtest/gtest.h>
#include "dlc_core/dfs.h"

TEST(DfsTest, NumIslands) {
    std::vector<std::vector<char>> grid1, grid2;

    grid1 = {
        {'1','0','1','0','0'},
        {'1','0','1','1','1'},
        {'1','1','0','1','1'},
        {'1','0','0','1','0'}
    };
    EXPECT_EQ(numIslands(grid1), 2);

    grid2 = {
    {'1','1','0','0','0'},
    {'1','1','0','0','0'},
    {'0','0','1','0','0'},
    {'0','0','0','1','1'}
    };
    EXPECT_EQ(numIslands(grid2), 3);
}