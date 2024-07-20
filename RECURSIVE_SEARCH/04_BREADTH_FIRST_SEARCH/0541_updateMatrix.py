class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dist = [[0] * m for _ in range(n)]
        q = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        def neighbor(x: int, y: int) -> Tuple[[int, int]]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        while q:
            x, y = q.popleft()
            visited.add((x, y))
            for dx, dy in neighbor(x, y):
                if mat[dx][dy] == 1 and (dx, dy) not in visited:
                    dist[dx][dy] = dist[x][y] + 1
                    visited.add((dx, dy))
                    q.append((dx, dy))
        
        return dist
