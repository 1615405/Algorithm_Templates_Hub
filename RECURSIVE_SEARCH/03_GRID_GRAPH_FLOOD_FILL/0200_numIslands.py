class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def bfs(sx: int, sy: int) -> int:
            from collections import deque
            q = deque([(sx, sy)])
            while q:
                x, y = q.popleft()
                grid[x][y] = "0"
                for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        q.append((nx, ny))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        
        return ans