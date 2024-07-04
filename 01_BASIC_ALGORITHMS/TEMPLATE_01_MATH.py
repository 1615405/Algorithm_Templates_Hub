def is_palindrome(x: int) -> bool:
    """
    检查给定的整数是否是回文数。
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10
    
    return x == reverted_number or reverted_number // 10 == x



def my_pow(base: float, exponent: int) -> float:
    """
    计算并返回 base 的 exponent 次方。
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



def largest_triangle_area(points: List[List[int]]) -> float:
    """
    计算给定点集中所有可能三角形的最大面积。
    """
    from itertools import combinations
    def triangle_area(p1: List[int], p2: List[int], p3: List[int]) -> float:
        import numpy as np
        matrix = np.array([p1 + [1], p2 + [1], p3 + [1]])
        return 0.5 * abs(np.linalg.det(matrix))
    
    return max(triangle_area(p1, p2, p3) for p1, p2, p3 in combinations(points, 3))



def trailing_zeroes(n: int) -> int:
    """
    计算 n!（n 的阶乘）的尾随零的数量。
    """
    zero_count = 0
    while n:
        zero_count += n // 5
        n //= 5
    return zero_count



def gcd(a: int, b: int) -> int:
    """
    计算两个整数的最大公约数（Greatest Common Divisor）。
    """
    if a == 0:
        return b
    return gcd(b % a, a)



def boyer_moore(nums: List[int]) -> int:
    """
    使用摩尔投票法找出数组中的多数元素。
    """
    # 初始阶段：候选人为空，计数器为0
    candidate = None
    count = 0

    # 第一阶段：找到可能的多数元素
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # 第二阶段：验证候选人是否为多数元素
    count = sum(1 for num in nums if num == candidate)
    
    # 确认候选人是否真的是多数元素
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found")