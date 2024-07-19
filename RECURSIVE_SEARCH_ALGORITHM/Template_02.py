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
