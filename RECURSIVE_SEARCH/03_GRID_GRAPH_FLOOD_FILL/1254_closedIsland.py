class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:  return 0

        def dfs(x: int, y: int) -> None:
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                nonlocal closed
                closed = False
            grid[x][y] = 1
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 0:
                    dfs(dx, dy)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    closed = True
                    dfs(i, j)           
                    ans += closed
        
        return ans
