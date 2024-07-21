class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 0
            s = grid[x][y]
            grid[x][y] = 0
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                s += dfs(dx, dy)
            return s
        
        return max(dfs(i, j) for i in range(n) for j in range(m))



class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def neighbor(x: int, y: int) -> int:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def bfs(x: int, y: int) -> int:
            q = deque([(x, y)])
            fishes = grid[x][y]
            grid[x][y] = 0
            while q:
                xx, yy = q.popleft()
                for dx, dy in neighbor(xx, yy):
                    if grid[dx][dy]:
                        q.append((dx, dy))
                        fishes += grid[dx][dy]
                        grid[dx][dy] = 0
            return fishes
        
        return max(bfs(i, j) if grid[i][j] else 0 for j in range(m) for i in range(n))
