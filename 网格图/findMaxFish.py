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
