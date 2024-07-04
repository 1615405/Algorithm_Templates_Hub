def find_first_blue(left: int, right: int) -> int:
    """
    查找第一个蓝色元素的索引。
    二分查找过程中，不断收缩右边界直到找到第一个蓝色元素。
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
    查找最后一个红色元素的索引。
    二分查找过程中，不断收缩左边界直到找到最后一个红色元素。
    """
    while left < right:
        pivot = (left + right + 1) // 2
        if is_red(pivot):
            left = pivot  # 发现红色，向右扩展范围以寻找更晚的红色
        else:
            right = pivot - 1  # 当前位置为蓝色，向左收缩范围
    return left  # 最终返回最后一个红色元素的位置