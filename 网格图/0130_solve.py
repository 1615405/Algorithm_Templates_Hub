class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        starts = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i == 0 or i == n - 1 or j == 0 or j == m - 1):
                    starts.append((i, j))
        
        def neighbor(x: int, y: int) -> Tuple[int, int]:
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx, dy
        
        def bfs(starts: List[Tuple[int, int]]) -> None:
            q = deque(starts)
            while q:
                xx, yy = q.popleft()
                board[xx][yy] = "A"
                for dx, dy in neighbor(xx, yy):
                    if board[dx][dy] == "O":
                        board[dx][dy] = "A"
                        q.append((dx, dy))
        
        bfs(starts)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
