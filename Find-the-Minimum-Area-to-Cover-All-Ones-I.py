class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        min_x = rows
        max_x = -1
        min_y = cols
        max_y = -1

        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == 1:
                    min_x = min(min_x,i)
                    max_x = max(min_x,i)
                    min_y = min(min_y,j)
                    max_y = max(max_y,j)
        
        w = max_x - min_x + 1
        h = max_y - min_y + 1
        a = w * h

        return a