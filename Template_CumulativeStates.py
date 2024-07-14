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


def findShortestSubArray(self, nums: List[int]) -> int:
    """
    找到具有相同度的最短子数组的长度。度是指数组中任一元素出现的最大频率。

    参数:
        nums (List[int]): 整数数组。

    返回:
        int: 具有相同度的最短子数组的长度
    """
    from collections import Counter
    first, last = {}, {}
    count = Counter(nums)

    for i, num in enumerate(nums):
        if num not in first:
            first[num] = i
        last[num] = i
    
    degree = max(count.values())
    min_length = len(nums)
    
    for num, cnt in count.items():
        if cnt == degree:
            min_length = min(min_length, last[num] - first[num] + 1)
    return min_length
