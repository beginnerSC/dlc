
def numIslands(grid):
    m = len(grid)
    n = len(grid[0])

    def paint(i, j):
        if grid[i][j]=='1':
            grid[i][j] = '2'
            if i>0   and grid[i-1][j]=='1':   paint(i-1, j)
            if i<m-1 and grid[i+1][j]=='1':   paint(i+1, j)
            if j>0   and grid[i][j-1]=='1':   paint(i, j-1)
            if j<n-1 and grid[i][j+1]=='1':   paint(i, j+1)

            return 1
        else:
            return 0
    
    return sum(paint(i, j) for i in range(m) for j in range(n))
        