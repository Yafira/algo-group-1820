#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target): # o(m + n)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        rows are sorted from left to right
        columns are sorted from top to bottom

        intuition: search from the top-right corner.
        if current cell M[r][c] is smaller than target x, then there is no need to look back at M[r][:c] because all cells on the left must be smaller than M[r][c]. So x must be somewhere in the cells below the current row; we can safely update r += 1.
        keep going down until M[r][c] is greater than x, at which point we look to the left to find the target. we can forget about the next rows because M[r:][c] are all greater than the current cell.

        lastly, return false if we haven't found the target by the time we reach the bottom left.
        """
        m, n = len(matrix), len(matrix) and len(matrix[0])
        r, c = 0, n - 1 # c represents the rightmost element in a row. r represnets the first row
        while r < m and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False
# @lc code=end

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
matrix = []
ans = Solution().searchMatrix(matrix, 5)
# ans = Solution().searchMatrix(matrix, 20)
ans = Solution().searchMatrix(matrix, 0)
print(ans)