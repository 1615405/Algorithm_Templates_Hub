class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        starts = []
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i == 0 or i == n - 1 or j == 0 or j == m - 1):
                    starts.append((i, j))

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def bfs(starts: List[Tuple[int, int]]) -> None:
            q = deque(starts)
            while q:
                xx, yy = q.popleft()
                grid[xx][yy] = 0
                for dx, dy in neighbor(xx, yy):
                    if grid[dx][dy] == 1:
                        q.append((dx, dy))
                        grid[dx][dy] = 0
        
        bfs(starts)

        return sum(grid[i][j] == 1 for j in range(m) for i in range(n))
