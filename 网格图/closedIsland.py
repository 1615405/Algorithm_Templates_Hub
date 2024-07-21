class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def bfs(x: int, y: int) -> bool:
            closed = True
            q = deque([(x, y)])
            grid[x][y] = 1
            while q:
                xx, yy = q.popleft()
                if xx == 0 or xx == n - 1 or yy == 0 or yy == m - 1:
                    closed = False
                for dx, dy in neighbor(xx, yy):
                    if grid[dx][dy] == 0:
                        grid[dx][dy] = 1
                        q.append((dx, dy))
            return closed
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    closed = bfs(i, j)
                    ans += closed
        
        return ans
