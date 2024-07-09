# ****************** 检查整数是否为回文 ******************
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
# ****************** End of 检查整数是否为回文 ******************



# ****************** 计算幂函数 ******************
def my_pow(base: float, exponent: int) -> float:
    """
    计算并返回 base 的 exponent 次方。
    """
    def power(base: float, exponent: int) -> float:
        ans = 1
        while exponent:
            if exponent & 1:
                ans *= base
            exponent >>= 1
            base *= base
        return ans

    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    return power(base, exponent)
# ****************** End of 计算幂函数 ******************



# ****************** 计算给定点集中所有可能三角形的最大面积 ******************
def largest_triangle_area(points: List[List[int]]) -> float:
    """
    计算给定点集中所有可能三角形的最大面积。
    """
    from itertools import combinations
    def triangle_area(p1, p2, p3):
        import numpy as np
        matrix = np.array([p1 + [1], p2 + [1], p3 + [1]])
        return 0.5 * abs(np.linalg.det(matrix))
    
    return max(triangle_area(p1, p2, p3) for p1, p2, p3 in combinations(points, 3))
# ****************** End of 计算给定点集中所有可能三角形的最大面积 ******************



# ****************** 计算 n! 的尾随零的数量 ******************
def trailing_zeroes(n: int) -> int:
    """
    计算 n!（n 的阶乘）的尾随零的数量。
    """
    zero_count = 0
    while n:
        zero_count += n // 5
        n //= 5
    return zero_count
# ****************** End of 计算 n! 的尾随零的数量 ******************



# ****************** 计算两个整数的最大公约数 ******************
def gcd(a: int, b: int) -> int:
    """
    计算两个整数的最大公约数（Greatest Common Divisor）。
    """
    if a == 0:
        return b
    return gcd(b % a, a)
# ****************** End of 计算两个整数的最大公约数 ******************



# ****************** 使用摩尔投票法找出数组中的多数元素 ******************
def boyer_moore(nums: List[int]) -> int:
    """
    使用摩尔投票法找出数组中的多数元素。
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # 验证候选人是否真的是多数元素
    count = sum(1 for num in nums if num == candidate)
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found")
# ****************** End of 使用摩尔投票法找出数组中的多数元素 ***********



# ****************** 计算具有与整个数组相同的度的最短子数组的长度 *******************
def findShortestSubArray(nums: List[int]) -> int:
    """
    计算具有与整个数组相同的度的最短子数组的长度。数组的“度”是数组中任一元素出现频率的最大值。
    此函数找到所有具有此度的子数组，并返回最短的那个的长度。

    参数:
    nums (List[int]): 输入的整数列表。

    返回:
    int: 具有与整个数组相同的度的最短子数组的长度。
    """
    first, last = {}, {}  # 存储每个元素的第一次和最后一次出现的索引
    count = Counter(nums)  # 计算每个元素的出现频率

    for i, num in enumerate(nums):
        if num not in first:
            first[num] = i  # 记录第一次出现的索引
        last[num] = i  # 更新最后一次出现的索引
    
    degree = max(count.values())  # 数组的度
    min_length = len(nums)  # 初始最小长度为数组长度

    for num, cnt in count.items():
        if cnt == degree:
            min_length = min(min_length, last[num] - first[num] + 1)

    return min_length
# ****************** End of 计算具有与整个数组相同的度的最短子数组的长度 ******************



# ****************** 计算字符串中每个字符到指定字符的最短距离 ******************
def shortest_distance_to_char(s: str, target_char: str) -> List[int]:
    """
    计算字符串中每个字符到指定字符的最短距离。此函数两次遍历字符串，首先从左向右记录到最近的目标字符的距离，
    然后从右向左更新这个距离以包括右侧目标字符的影响。

    参数:
    s (str): 输入字符串。
    target_char (str): 指定的目标字符。

    返回:
    List[int]: 每个字符到指定字符的最短距离数组。
    """
    n = len(s)
    min_distances = [float('inf')] * n  # 初始化距离数组为无限大
    
    last_seen_left = float('-inf')  # 左侧最近看到的目标字符索引
    for i in range(n):
        if s[i] == target_char:
            last_seen_left = i
        min_distances[i] = i - last_seen_left
    
    last_seen_right = float('inf')  # 右侧最近看到的目标字符索引
    for i in range(n-1, -1, -1):
        if s[i] == target_char:
            last_seen_right = i
        min_distances[i] = min(min_distances[i], last_seen_right - i)
    
    return min_distances
# ****************** End of 计算字符串中每个字符到指定字符的最短距离 ******************