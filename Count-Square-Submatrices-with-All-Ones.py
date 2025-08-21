import numpy as np

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        squares_at = np.zeros((m, n), dtype=int)
        total_squares = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # edge (literally) cases
                    if i == 0 or j == 0:
                        squares_at[i][j] = 1
                    else:
                        top = squares_at[i][j-1]
                        left = squares_at[i-1][j]
                        diag = squares_at[i-1][j-1]
                        squares_at[i][j] = min(top,left,diag) + 1
                    total_squares += squares_at[i][j]

        return int(total_squares)