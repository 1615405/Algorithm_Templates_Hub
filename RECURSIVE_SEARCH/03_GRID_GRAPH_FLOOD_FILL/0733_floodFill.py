class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m, curr_color = len(image), len(image[0]), image[sr][sc]

        if curr_color == color:
            return image
        
        def dfs(x: int, y: int) -> None:
            image[x][y] = color
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == curr_color:
                    dfs(nx, ny)
        
        dfs(sr, sc)
        return image
