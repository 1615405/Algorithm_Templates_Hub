def my_pow(base: float, exponent: int) -> float:
    """
    计算并返回 base 的 exponent 次方。

    Args:
        base (float): 计算的基数。
        exponent (int): 计算的指数。

    Returns:
        float: base 的 exponent 次幂。
    """
    def power(base: float, exponent: int) -> float:
        ans = 1
        while exponent:
            if exponent & 1:  # 当前指数的最低位是1时，将当前基数乘到结果中
                ans = ans * base
            exponent >>= 1  # 指数右移一位，相当于除以2
            base = base * base  # 基数自身相乘，相当于指数翻倍
        return ans

    # 处理指数为负数的情况
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    return power(base, exponent)