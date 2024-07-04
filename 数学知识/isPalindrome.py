def is_palindrome(x: int) -> bool:
    """
    检查给定的整数是否是回文数。
    
    回文数指的是正向和反向读都一样的数。
    
    参数:
        x (int): 需要检查的整数。

    返回:
        bool: 如果该整数是回文数，返回 True；否则返回 False。
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10
    
    return x == reverted_number or reverted_number // 10 == x