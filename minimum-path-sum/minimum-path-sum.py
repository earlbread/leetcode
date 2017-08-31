class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        table = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i - 1 < 0 and j - 1 < 0:
                    table[i][j] = grid[i][j]
                elif i - 1 < 0:
                    table[i][j] = grid[i][j] + table[i][j-1]
                elif j - 1 < 0:
                    table[i][j] = grid[i][j] + table[i-1][j]
                else:
                    up = table[i-1][j]
                    left = table[i][j-1]

                    table[i][j] = grid[i][j] + min(up, left)
        return table[m-1][n-1]

s = Solution()
assert(s.minPathSum([[0]]) == 0)
assert(s.minPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 21)
