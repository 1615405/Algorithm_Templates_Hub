class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i, j))
        
        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited:
                    yield dx, dy
        
        ans = 0
        while q:
            x, y, d = q.popleft()
            for dx, dy in neighbor(x, y):
                if grid[dx][dy] == 1:
                    q.append((dx, dy, d + 1))
                    visited.add((dx, dy))
                    grid[dx][dy] = 2

            ans = max(ans, d)
        
        return ans if not any(1 in row for row in grid) else -1
