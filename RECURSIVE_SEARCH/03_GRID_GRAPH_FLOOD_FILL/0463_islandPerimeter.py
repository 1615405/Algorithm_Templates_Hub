class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0
            grid[x][y] = 2
            perimeter = 0
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                perimeter += dfs(dx, dy)
            return perimeter
        
        perimeter = 0
        for i in range(n):
            for j in range(m):
                perimeter += dfs(i, j) if grid[i][j] == 1 else 0
        return perimeter
