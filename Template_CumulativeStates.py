def maxProfit(prices: List[int]) -> int:
    """
    买卖股票的最佳时机。
    
    参数：
        prices (List[int]): 每日股票价格的列表。
    
    返回：
        int: 可以从这一次交易中获得的最大利润。
    """
    ans = 0
    min_price = prices[0]
    for p in prices:
        ans = max(ans, p - min_price)
        min_price = min(min_price, p)
    return ans


class NumArray:
    """
    利用前缀和数组优化区间和查询的类。
    """
    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right+1] - self.s[left]
