class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        original_color = grid[row][col]
        borders = []
        visited = set()

        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def modify_color(x: int, y: int) -> bool:
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                return True
            return not all(grid[x][y] == grid[dx][dy] for dx, dy in neighbor(x, y))
        
        
        def dfs(x: int, y: int) -> None:
            if (x, y) in visited:
                return
            if modify_color(x, y):
                borders.append((x, y))
            visited.add((x, y))
            for dx, dy in neighbor(x, y):
                if grid[dx][dy] == original_color:
                    dfs(dx, dy)
        
        
        if original_color == color:
            return grid

        dfs(row, col)

        for x, y in borders:
            grid[x][y] = color

        return grid
