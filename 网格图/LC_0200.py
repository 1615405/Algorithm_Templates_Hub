class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def dfs(x: int, y: int) -> None:
            grid[x][y] = "0"
            for dx, dy in neighbor(x, y):
                if grid[dx][dy] == "1":
                    dfs(dx, dy)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def bfs(x: int, y: int) -> int:
            q = deque([(x, y)])
            grid[x][y] = "0"
            while q:
                x, y = q.popleft()
                for dx, dy in neighbor(x, y):
                    if grid[dx][dy] == "1":
                        q.append((dx, dy))
                        grid[dx][dy] = "0"
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1

        return ans
