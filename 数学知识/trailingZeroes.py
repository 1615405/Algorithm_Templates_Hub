def trailing_zeroes(n: int) -> int:
    """
    计算 n!（n 的阶乘）的尾随零的数量。
    
    由于尾随零是由因子 5 和 2 形成的，而在阶乘中因子 2 的数量总是多于因子 5，
    因此只需计算包含的因子 5 的数量即可确定尾随零的数量。
    
    Args:
        n (int): 阶乘的上界。

    Returns:
        int: 尾随零的数量。
    """
    zero_count = 0
    while n:
        zero_count += n // 5
        n //= 5
    return zero_count