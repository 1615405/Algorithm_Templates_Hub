def readBinaryWatch(turnedOn: int) -> List[str]:
    """
    计算所有可能的时间，其中二进制表示中有指定数量的 1s 的灯被点亮。
    
    参数:
        turnedOn (int): 点亮的灯的数量，这些灯在二进制表达的小时和分钟上。
    
    返回:
        List[str]: 表示所有可能时间的字符串列表，格式为 "小时:分钟"，分钟保留两位数。
    """
    ans = list()
    for i in range(1024):  # 1024 = 2^10，因为总共有 10 个灯（4 个小时灯，6 个分钟灯）
        h, m = i >> 6, i & 0x3f  # 提取小时数和分钟数
        if h < 12 and m < 60 and bin(i).count("1") == turnedOn:  # 验证时间的有效性和点亮灯的数量
            ans.append(f"{h}:{m:02d}")  # 格式化输出并添加到结果列表
    return ans


def islandPerimeter(grid: List[List[int]]) -> int:
    """
    计算在给定的二维网格中，由1组成的岛屿的周长。
    
    参数:
        grid (List[List[int]]): 二维网格，其中1表示陆地，0表示水。每个单元格是正方形，边长为1。
    
    返回:
        int: 岛屿的周长。
    
    描述:
    通过深度优先搜索（DFS）遍历网格中的每个陆地单元格，并计算其对周长的贡献。每个陆地单元格会检查其四个方向（上、下、左、右），每朝一个方向走到边界或水域时，
    周长加1。如果该方向的单元格已访问过或为水，这部分边界也算入周长。为防止重复访问，访问过的陆地单元格将其值标记为2。
    """
    m, n = len(grid), len(grid[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = 0
    
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


def isOneBitCharacter(bits: List[int]) -> bool:
    """
    判断由 1-bit 和 2-bit 组成的数组中最后一个字符是否为一个 1-bit 字符。

    参数:
        bits (List[int]): 一个整数数组，其中每个整数只能是 0 或 1。数组中的数字代表一个数据流，其中 0 代表一个 1-bit 的字符，10 或 11 代表一个 2-bit 的字符。

    返回:
        bool: 如果数组的最后一个字符是一个 1-bit 字符，则返回 True；否则返回 False。
    """
    n = len(bits)
    @cache
    def can_decode(start: int) -> bool:
        if start == n - 1:
            return bits[start] == 0
        if start >= n:
            return False
        if bits[start] == 0:
            return can_decode(start + 1)
        if start + 1 < n and bits[start] == 1:
            return can_decode(start + 2)
    return can_decode(0)


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    对图像执行“泛洪填充”操作。
    
    参数:
        image (List[List[int]]): 二维整数数组，代表图像的像素值。
        sr (int): 起始像素的行号。
        sc (int): 起始像素的列号。
        color (int): 要填充的颜色值。
    
    返回:
        List[List[int]]: 修改后的图像。
    """
    currColor = image[sr][sc]
    if currColor == color:
        return image
    n, m = len(image), len(image[0])
    que = collections.deque([(sr, sc)])
    image[sr][sc] = color
    while que:
        x, y = que.popleft()
        for mx, my in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                image[mx][my] = color
                que.append((mx, my))
    return image


def minCostClimbingStairs(self, cost: List[int]) -> int:
    """
    计算爬楼梯的最小成本。可以从索引0或1开始，每次可以爬1或2个台阶。
    
    参数:
        cost (List[int]): 每一阶台阶的登上成本。
    
    返回:
        int: 爬完所有台阶后的最小成本。
    
    描述:
    使用深度优先搜索（DFS）结合记忆化（缓存）来寻找达到楼梯顶部的最小成本。基本思路是，到达最顶层可以从最后一阶或倒数第二阶完成。
    因此，我们可以使用递归来解决这个问题，并且使用 @cache 装饰器来存储之前计算的结果，避免重复计算。
    """
    @cache
    def dfs(i: int) -> int:
        if i <= 1:
            return 0
        return min(dfs(i - 2) + cost[i - 2], dfs(i - 1) + cost[i - 1])
    return dfs(len(cost))
