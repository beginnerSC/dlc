#include "dlc_core/dfs.h"
#include <vector>
#include <functional>

int numIslands(std::vector<std::vector<char>>& grid) {
    int m = grid.size();
    int n = grid[0].size();

    std::function<int(int, int)> paint = [&](int i, int j){
        if (grid[i][j]=='1') {
            grid[i][j] = '2';
            if ( i > 0   && grid[i-1][j]=='1' )   paint(i-1, j);
            if ( i < m-1 && grid[i+1][j]=='1' )   paint(i+1, j);
            if ( j > 0   && grid[i][j-1]=='1' )   paint(i, j-1);
            if ( j < n-1 && grid[i][j+1]=='1' )   paint(i, j+1);

            return 1;
            
        } else {
            return 0;
        }
    };

    int res = 0;
    for (int i=0 ; i<m ; ++i) {
        for (int j=0 ; j<n ; ++j) {
            res += paint(i, j);
        }
    }
    return res;
}