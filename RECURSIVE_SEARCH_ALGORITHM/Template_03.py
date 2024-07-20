def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    对图像执行泛洪填充操作。
    """
    curr_color = image[sr][sc]
    if curr_color == color:
        return image
    
    n, m = len(image), len(image[0])
    q = deque([(sr, sc)])
    image[sr][sc] = color
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == curr_color:
                image[nx][ny] = color
                q.append((nx, ny))
                
    return image
    

def islandPerimeter(grid: List[List[int]]) -> int:
    """
    计算在给定的二维网格中, 由1组成的岛屿的周长。
    """
    n, m = len(grid), len(grid[0])
    
    def dfs(x: int, y: int) -> int:
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 1
        if grid[x][y] == 2:
            return 0
        grid[x][y] = 2
        perimeter = 0
        for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            perimeter += dfs(dx, dy)
        return perimeter
    
    perimeter = 0
    for i in range(n):
        for j in range(m):
            perimeter += dfs(i, j) if grid[i][j] == 1 else 0
    return perimeter


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    计算二维网格中最大的岛屿面积。岛屿由相邻的陆地组成，陆地由“1”表示，水域由“0”表示。岛屿可以在水平或垂直方向相邻，但不能对角相连。
    """
    n, m = len(grid), len(grid[0])
    
    def dfs(x: int, y: int) -> int:
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        ans = 1
        for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            ans += dfs(dx, dy)
        return ans
    
    max_area = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))
    
    return max_area


def numIslands(grid: List[List[str]]) -> int:
    """
    计算给定的二维网格中岛屿的数量。一个岛被定义为由相邻的陆地组成的组合，且被水域四面环绕。
    这里的相邻仅指在水平或垂直方向上相连的陆地。使用广度优先搜索(BFS)来遍历找到所有的岛屿。
    """
    n, m = len(grid), len(grid[0])
    visited = set()
    
    def bfs(x: int, y: int) -> None:
        q = deque([(x, y)])
        visited.add((x, y))
        while q:
            x, y = q.popleft()
            grid[x][y] = "0"
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == "1" and (dx, dy) not in visited:
                    q.append((dx, dy))
                    visited.add((dx, dy))
                    
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                bfs(i, j)
                ans += 1
    return ans


def closedIsland(grid: List[List[int]]) -> int:
    """
    计算二维网格中完全被水包围的岛屿数量。岛屿定义为四面被水 1 包围的连续区域 0
    """
    n, m = len(grid), len(grid[0])
    if n < 3 or m < 3:  return 0

    def dfs(x: int, y: int) -> None:
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            nonlocal closed
            closed = False
        grid[x][y] = 1
        for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 0:
                dfs(dx, dy)
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                closed = True
                dfs(i, j)           
                ans += closed
    return ans


def solve(board: List[List[str]]) -> None:
    """
    直接修改给定的二维棋盘，将所有不连接到边界的 'O' 转换成 'X'。
    从棋盘的边界开始，使用深度优先搜索（DFS）标记所有连接到边界的 'O'。
    """
    n, m = len(board), len(board[0])
    def dfs(x: int, y: int) -> None:
        if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != "O":
            return
        board[x][y] = "A"
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    for i in range(n):
        dfs(i, 0)
        dfs(i, m - 1)
    
    for j in range(m - 1):
        dfs(0, j)
        dfs(n - 1, j)
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "A":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"
