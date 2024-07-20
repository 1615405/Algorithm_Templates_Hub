class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            ans = 1
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                ans += dfs(dx, dy)
            return ans
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
