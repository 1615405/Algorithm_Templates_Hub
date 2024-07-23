class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        if fresh_count == 0:  return 0
        
        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        min_passed = 0
        while q:
            min_passed += 1
            for _ in range(len(q)):
                xx, yy = q.popleft()
                for nx, ny in neighbor(xx, yy):
                    if grid[nx][ny] == 1:
                        fresh_count -= 1
                        grid[nx][ny] = 2
                        q.append((nx, ny))
        
        return min_passed - 1 if not fresh_count else -1
