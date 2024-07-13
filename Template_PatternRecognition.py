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
