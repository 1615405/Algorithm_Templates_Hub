class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0 or visited[x][y]:
                return
            visited[x][y] = True
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                dfs(dx, dy)
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        
        for j in range(m - 1):
            dfs(0, j)
            dfs(n - 1, j)
        
        return sum(grid[i][j] == 1 and not visited[i][j] for j in range(1, m - 1) for i in range(1, n - 1))
