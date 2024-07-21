class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        n, m = len(land), len(land[0])
        ans = list()

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        yield nx, ny
        
        def dfs(x: int, y: int):
            ans = 1
            land[x][y] = 1
            for dx, dy in neighbor(x, y):
                if land[dx][dy] == 0:
                    ans += dfs(dx, dy)
            return ans
        
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    ans.append(dfs(i, j))
        
        return sorted(ans)
