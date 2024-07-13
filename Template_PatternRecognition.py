def find_first_blue(left: int, right: int) -> int:
    """
    查找第一个蓝色元素的索引。二分查找过程中，不断收缩右边界直到找到第一个蓝色元素。
    """
    while left < right:
        pivot = (left + right) // 2
        if is_blue(pivot):
            right = pivot  # 发现蓝色，尝试向左收缩范围以寻找更早的蓝色
        else:
            left = pivot + 1  # 当前位置为红色，向右继续搜索
    return left  # 最终返回第一个蓝色元素的位置


def find_last_red(left: int, right: int) -> int:
    """
    查找最后一个红色元素的索引。二分查找过程中，不断收缩左边界直到找到最后一个红色元素。
    """
    while left < right:
        pivot = (left + right + 1) // 2
        if is_red(pivot):
            left = pivot  # 发现红色，向右扩展范围以寻找更晚的红色
        else:
            right = pivot - 1  # 当前位置为蓝色，向左收缩范围
    return left  # 最终返回最后一个红色元素的位置


def majorityElement(nums):
    """
    利用摩尔投票法找出列表中的多数元素。多数元素是指在数组中出现次数超过一半的元素。

    参数：
        nums (List[int]): 输入的整数列表。

    返回：
        int: 数组中的多数元素。
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
    
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found")


def thirdMax(nums: List[int]) -> int:
    """
    找出数组中第三大的数。如果不存在第三大的数，则返回最大数。

    参数:
    nums (List[int]): 输入的整数数组。

    返回:
    int: 数组中第三大的数，或者如果不足三个不同的数，则返回最大数。
    """
    from sortedcontainers import SortedList
    s = SortedList()
    for num in nums:
        if num not in s:
            s.add(num)
            if len(s) > 3:  s.pop(0)
    return s[0] if len(s) == 3 else s[-1]


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    """
    在一个给定的从1到n的数组中，找出所有未出现在数组中的数字。
    
    参数:
    nums (List[int]): 一个范围从 1 到 n 的整数数组，但数组中的一些元素可能丢失或重复。
    
    返回:
    List[int]: 数组中没有出现的数字列表。
    """
    n = len(nums)
    for num in nums:
        x = (num - 1) % n
        nums[x] += n
    return [i + 1 for i, num in enumerate(nums) if num <= n]


def repeatedSubstringPattern(s: str) -> bool:
    """
    检查给定字符串是否可以由它的一个子字符串重复多次构成。
    
    参数:
    s (str): 输入的字符串。
    
    返回:
    bool: 如果字符串可以由它的一个子字符串重复构成，则返回 True，否则返回 False。
    
    描述:
    使用 Knuth-Morris-Pratt (KMP) 算法的部分匹配表（也称为失配表）来寻找可能的重复模式。
    首先通过构建失配表来判断字符串的周期性。然后检查字符串的长度是否能被周期长度整除，
    来确定整个字符串是否由重复的子字符串构成。此外，还有一个快速检查，通过将字符串加倍
    并移除首尾字符后，看原字符串是否存在于新字符串中，这是基于字符串周期性的一个快速验证方法。
    """
    def build_kmp_fail(pattern: str) -> list:
        m = len(pattern)
        fail = [-1] * m
        for i in range(1, m):
            j = fail[i - 1]
            while j != -1 and pattern[j + 1] != pattern[i]:
                j = fail[j]
            if pattern[j + 1] == pattern[i]:
                fail[i] = j + 1
        return fail
        
    def check(s: str) -> bool:
        doubled_s = (s + s)[1:-1]
        return s in doubled_s
    
    n = len(s)
    fail = build_kmp_fail(s)
    lps = (fail)[-1] + 1
    return lps > 0 and n % (n - lps) == 0


def checkPerfectNumber(num: int) -> bool:
    """
    检查给定的数字是否是完美数。完美数是指真正因子（除了自身以外的约数）之和等于它本身的正整数。
    
    参数:
        num (int): 需要检查的数字。
    
    返回:
        bool: 如果 num 是完美数，则返回 True，否则返回 False。
    """
    perfect_numbers = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]
    return num in perfect_numbers
