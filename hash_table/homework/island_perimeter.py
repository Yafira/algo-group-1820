# https://leetcode.com/problems/island-perimeter

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land = 0
        stripe = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    land += 1
                    if i > 0 and grid[i-1][j] == 1:
                        stripe += 1
                    if j > 0 and grid[i][j-1] == 1:
                        stripe += 1
        return land * 4 - stripe * 2
