def isOneBitCharacter(bits: List[int]) -> bool:
    """
    判断由 1-bit 和 2-bit 组成的数组中最后一个字符是否为一个 1-bit 字符。
    """
    n = len(bits)

    @cache
    def can_decode(start: int) -> bool:
        if start == n - 1:
            return bits[start] == 0
        if start == n:
            return False
        if bits[start] == 0:
            return can_decode(start + 1)
        if start < n - 1 and bits[start] == 1:
            return can_decode(start + 2)
    
    return can_decode(0)


def minCostClimbingStairs(cost: List[int]) -> int:
    """
    计算爬楼梯的最小成本。可以从索引0或1开始, 每次可以爬1或2个台阶。
    """
    
    @cache
    def dfs(i: int) -> int:
        if i <= 1:
            return 0
        return min(dfs(i - 2) + cost[i - 2], dfs(i - 1) + cost[i - 1])
    
    return dfs(len(cost))


def minimumOperationsToMakeEqual(x: int, y: int) -> int:
    """
    计算将整数 x 转换为整数 y 的最小操作次数。操作包括：
    1. 直接增加或减少 x 至 y。
    2. 通过对 x 进行除以 11 或 5 后再进行必要的加减操作以逼近 y。
    """
    @cache
    def dfs(x: int, y: int) -> int:
        if x <= y:  return y - x
        return min(x - y,
                dfs(x // 11, y) + x % 11 + 1,
                dfs(x // 11 + 1, y) + 11 - x % 11 + 1,
                dfs(x // 5, y) + x % 5 + 1,
                dfs(x // 5 + 1, y) + 5 - x % 5 + 1
        )
    
    return dfs(x, y)


 def minDays(n: int) -> int:
    """
    计算将整数 n 减少到 1 所需的最小天数。每天你可以执行以下操作之一：
    1. 如果 n 是 2 的倍数，你可以将 n 减半。
    2. 如果 n 是 3 的倍数，你可以将 n 减为 n 的三分之一。
    3. 减少 n 的值为 1。
    """
    @cache
    def dfs(n: int) -> int:
        if n <= 1:  return n
        return min(dfs(n // 2) + n % 2, dfs(n // 3) + n % 3) + 1
    
    return dfs(n)
