class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set(starts)
            q = deque(starts)
            while q:
                x, y = q.popleft()
                for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if 0 <= dx < n and 0 <= dy < m and heights[dx][dy] >= heights[x][y] and (dx, dy) not in visited:
                        q.append((dx, dy))
                        visited.add((dx, dy))
            
            return visited
        
        pacific = [(0, j) for j in range(m)] + [(j, 0) for j in range(1, n)]
        atlantic = [(i, m - 1) for i in range(n)] + [(n - 1, i) for i in range(m - 1)]

        return list(bfs(pacific) & bfs(atlantic))