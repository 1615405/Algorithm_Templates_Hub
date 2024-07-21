class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def dfs(x: int, y: int) -> int:
            ans = 1
            grid[x][y] = 0
            for dx, dy in neighbor(x, y):
                if grid[dx][dy] == 1:
                    ans += dfs(dx, dy)
            return ans
        
        return max(dfs(i, j) if grid[i][j] == 1 else 0 for j in range(m) for i in range(n))



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def bfs(x: int, y: int) -> int:
            cnt = 1
            q = deque([(x, y)])
            grid[x][y] = 0
            while q:
                i, j = q.popleft()
                for dx, dy in neighbor(i, j):
                    if grid[dx][dy] == 1:
                        cnt += 1
                        q.append((dx, dy))
                        grid[dx][dy] = 0
            return cnt

        return max(bfs(i, j) if grid[i][j] == 1 else 0 for j in range(m) for i in range(n))
