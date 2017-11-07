class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def pathLen(matrix, l, row, col):
            if l[row][col] > 0:
                return l[row][col]

            dirs = [(-1, 0), (1, 0), (0, -1,), (0, 1)]
            max_path = 1

            for d in dirs:
                r = row + d[0]
                c = col + d[1]

                if (r < 0 or c < 0 or
                    r >= len(matrix) or c >= len(matrix[0]) or
                    matrix[r][c] > matrix[row][col]):
                    continue

                path = pathLen(matrix, l, r, c)
                max_path = max(path, max_path)

            l[row][col] = max_path
            return max_path

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        l = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                pathLen(matrix, l, i, j)

        return max(map(max, l))

s = Solution()

arrays = [
        [],
        [[1]],
        [[2]],
        [[1,2]],
        [[2,1]],
        [[9,9,4],[6,6,8],[2,1,1]],
        [[3,4,5],[3,2,6],[2,2,1]]
        ]

for a in arrays:
    print(s.longestIncreasingPath(a))
