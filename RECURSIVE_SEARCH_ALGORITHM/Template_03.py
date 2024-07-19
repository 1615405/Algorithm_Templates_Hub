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
    m, n = len(grid), len(grid[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def dfs(x: int, y: int) -> int:
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return 1
        if grid[x][y] == 2:
            return 0
        grid[x][y] = 2
        ans = 0
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            ans += dfs(tx, ty)
        return ans
    
    result = 0
    for i in range(m):
        for j in range(n):
            result += dfs(i, j) if grid[i][j] == 1 else 0
    return result
