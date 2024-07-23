class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        @cache
        def dfs(x: int, y: int) -> int:
            max_path = 1
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m and matrix[dx][dy] < matrix[x][y]:
                    max_path = max(max_path, dfs(dx, dy) + 1)

            return max_path
        
        return max(dfs(i, j) for j in range(m) for i in range(n))
