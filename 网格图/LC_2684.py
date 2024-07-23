class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        starts = [(i, 0) for i in range(n)]
        q = deque(starts)
        visited = set(starts)

        while q:
            xx, yy = q.popleft()
            for dx, dy in (xx - 1, yy + 1), (xx, yy + 1), (xx + 1, yy + 1):
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] > grid[xx][yy] and (dx, dy) not in visited:
                    q.append((dx, dy))
                    visited.add((dx, dy))
                    ans = dy
        
        return ans
