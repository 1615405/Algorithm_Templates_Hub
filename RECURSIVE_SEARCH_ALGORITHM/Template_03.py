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
