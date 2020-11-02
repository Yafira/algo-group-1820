#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0 # the perimeter
        m, n = map(len, (grid, grid[0])) # determine the length of the rows, and columsn
        def dfs(i, j): # depth first search
            stripes = 0 # recording the current number of the good boys.
            for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
                x += i
                y += j
                if x < 0 or x == m or y < 0 or y == n or not grid[x][y]: # is my neighbor a water? if so, increment the stripes by 1. 
                    stripes += 1
            return stripes
        for i in range(m):
            for j in range(n):
                if grid[i][j]: # an island is 1. if grid[i][j] == 1.
                    res += dfs(i, j)
        return res
# @lc code=end

