class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        visited = set()
        dist = [[0] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            x, y = q.popleft()
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1 and (nx, ny) not in visited:
                    dist[nx][ny] = dist[x][y] + 1
                    visited.add((nx, ny))
                    q.append((nx, ny))

        return dist
